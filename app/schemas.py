# schemas.py

from pydantic import BaseModel
from typing import List, Optional

class AnalyzeRequest(BaseModel):
    """
    Request model for analysis endpoint.
    """
    text: str

class AnalyzeResponse(BaseModel):
    """
    Response model for analysis endpoint.
    """
    paragraphs: int
    sentences: int
    words: int
    characters: int
    adverbs: int
    passive: int
    complex: int
    qualifiers: int
    readability_score: float

class Suggestion(BaseModel):
    """
    Single suggestion item for style improvements.
    """
    offset: Optional[int]
    length: int
    type: str
    suggestion: str

class SuggestResponse(BaseModel):
    """
    Response model for suggestions endpoint.
    """
    suggestions: List[Suggestion]

class RewriteRequest(BaseModel):
    """
    Request model for rewrite endpoint.
    """
    text: str

class RewriteResponse(BaseModel):
    """
    Response model for rewrite endpoint.
    """
    rewritten_text: str