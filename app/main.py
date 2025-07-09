# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from .analyzer import AnalysisResult, get_sentences, annotate_adverbs, annotate_passive, annotate_complex, calculate_level

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    readability_score: float
    adverb_count: int
    passive_voice_count: int
    complex_count: int
    hard_sentences: int
    very_hard_sentences: int

@app.post('/analyze', response_model=AnalyzeResponse)
def analyze(req: TextRequest):
    result = AnalysisResult()
    paragraphs = req.text.split('\n')
    result.paragraphs = len(paragraphs)
    for para in paragraphs:
        sentences = get_sentences(para)
        result.sentences += len(sentences)
        for sent in sentences:
            # strip punctuation and count letters/words for readability
            clean = re.sub(r'[^a-zA-Z0-9 ]', '', sent)
            words = len(clean.split())
            letters = len(clean.replace(' ', ''))
            result.words += words
            lvl = calculate_level(letters, words, 1)
            if words >= 14 and 10 <= lvl < 14:
                result.hardSentences += 1
            elif words >= 14 and lvl >= 14:
                result.veryHardSentences += 1
            # count features
            _, result.adverbs = annotate_adverbs(sent, result)
            _, result.passiveVoice = annotate_passive(sent, result)
            _, result.complex = annotate_complex(sent, result)
    readability = round(4.71 * (result.words / result.sentences) + 0.5 * (result.words / result.sentences) - 21.43, 2)
    return AnalyzeResponse(
        readability_score=readability,
        adverb_count=result.adverbs,
        passive_voice_count=result.passiveVoice,
        complex_count=result.complex,
        hard_sentences=result.hardSentences,
        very_hard_sentences=result.veryHardSentences
    )