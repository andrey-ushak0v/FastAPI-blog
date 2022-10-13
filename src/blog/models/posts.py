from datetime import date
from enum import Enum

from pydantic import BaseModel


class PostKind(str, Enum):
    STORY = 'story'
    LIFESTORY = 'lifestory'
    HUMOR = 'humor'
    TUTORIAL = 'tutorial'

class PostBase(BaseModel):
    date: date
    text: str
    kind: PostKind

class Post(PostBase):
    id: int
    
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Post_update(PostBase):
    pass