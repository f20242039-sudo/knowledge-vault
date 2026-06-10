"""
ai/schemas.py
Pydantic models that define and validate the structure of AI-generated tags.
If Groq returns invalid JSON or wrong types, these models catch it before DB writes.
"""

from pydantic import BaseModel, field_validator
from typing import Literal


class SkillTag(BaseModel):
    name: str
    coverage: int

    @field_validator("coverage")
    @classmethod
    def coverage_in_range(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("Coverage must be between 0 and 100")
        return v


class DocumentTagSchema(BaseModel):
    description: str
    difficulty: Literal["Beginner", "Intermediate", "Advanced"]
    subjects: list[str]
    skills: list[SkillTag]
