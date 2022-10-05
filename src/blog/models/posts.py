from datetime import date
from enum import Enum

from pydantic import BaseModel


class PostKind(str, Enum):
    STORY = 'story'
    LIFESTORY = 'lifestory'
    HUMOR = 'humor'
    TUTORIAL = 'tutorial'

class Post(BaseModel):
    id: int
    date: date
    text: str
    kind: PostKind

    class Config:
        orm_mode = True

    