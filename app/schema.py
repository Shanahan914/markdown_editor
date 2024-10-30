from pydantic import BaseModel 
from typing import List, Dict
from datetime import datetime

class NoteMetaPublic(BaseModel):
    id: int
    filename: str
    version: int
    uploaded : datetime


class ErrorDetail(BaseModel):
    offset: int
    message : str
    replacements : List[str]


class GrammarDataPublic(BaseModel):
    errors: Dict[int, ErrorDetail]
    corrected_version : str