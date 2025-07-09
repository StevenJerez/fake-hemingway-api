# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Use relative imports now that app/ is a package
from .analyzer import analyze_text, rewrite_text
from .schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    SuggestResponse,
    RewriteRequest,
    RewriteResponse,
    Suggestion
)

app = FastAPI(
    title="Hemingway-like API",
    description="API for text readability analysis, style suggestions, and simple rewrite",
    version="1.0.0"
)

# --- Schemas --- #

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    paragraphs: int
    sentences: int
    words: int
    adverbs: int
    passive: int
    complex: int
    qualifiers: int
    readability_score: float

class Suggestion(BaseModel):
    offset: Optional[int]
    length: int
    type: str
    suggestion: str

class SuggestResponse(BaseModel):
    suggestions: List[Suggestion]

class RewriteRequest(BaseModel):
    text: str

class RewriteResponse(BaseModel):
    rewritten_text: str

# --- App Initialization --- #

app = FastAPI(
    title="Hemingway-like API",
    description="API for text readability analysis, style suggestions, and simple rewrite",
    version="1.0.0"
)

# --- Endpoints --- #

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    """
    Analyze the given text and return readability metrics.
    """
    metrics, _ = analyze_text(req.text)
    return metrics

@app.post("/suggest", response_model=SuggestResponse)
def suggest(req: AnalyzeRequest):
    """
    Analyze the text and return a list of style suggestions
    such as adverbs, passive voice, complex phrases, and qualifiers.
    """
    _, suggestions = analyze_text(req.text)
    return {"suggestions": suggestions}

@app.post("/rewrite", response_model=RewriteResponse)
def rewrite(req: RewriteRequest):
    """
    Perform a simple rewrite by applying the first-pass
    simplifications: removing adverbs, converting passive voice,
    replacing one complex phrase, and removing qualifiers.
    """
    rewritten = rewrite_text(req.text)
    return {"rewritten_text": rewritten}