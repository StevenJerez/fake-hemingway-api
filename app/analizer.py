# app/analyzer.py
import re
from typing import List

def get_sentences(text: str) -> List[str]:
    parts = [s.strip() + '.' for s in text.split('. ') if s.strip()]
    return parts

# Implement calculateLevel, get_adverbs, get_passive, get_complex, etc.
# Use similar regex and scanning logic to mirror the JS behavior, updating counters inside a context object.

class AnalysisResult:
    def __init__(self):
        self.paragraphs = 0
        self.sentences = 0
        self.words = 0
        self.hardSentences = 0
        self.veryHardSentences = 0
        self.adverbs = 0
        self.passiveVoice = 0
        self.complex = 0

# Define functions to annotate and count: annotate_adverbs, annotate_passive, annotate_complex.
# Each should return the annotated string and update the counters in AnalysisResult.