# app/schemas.py
from pydantic import BaseModel, Field
from typing import List, Optional

class TextRequest(BaseModel):
    text: str = Field(..., description="Input text to analyze or transform")
    rules: Optional[List[str]] = Field(None, description="List of rules for /suggest")
    style: Optional[str] = Field(None, description="Target style for /rewrite")

class Suggestion(BaseModel):
    offset: int
    length: int
    type: str
    suggestion: str

class AnalyzeResponse(BaseModel):
    readability_score: float
    adverb_count: int
    passive_voice_count: int
    complex_count: int
    hard_sentences: int
    very_hard_sentences: int

class SuggestResponse(BaseModel):
    suggestions: List[Suggestion]

class RewriteResponse(BaseModel):
    rewritten_text: str