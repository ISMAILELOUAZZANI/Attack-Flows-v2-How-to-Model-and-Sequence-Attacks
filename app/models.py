from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class AttackStep(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = ""
    prerequisites: List[str] = []
    effects: List[str] = []

class AttackFlow(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = ""
    steps: List[AttackStep]
    edges: List[tuple] = []  # (from_step_id, to_step_id)