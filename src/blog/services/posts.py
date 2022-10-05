"""здесь хранится бизнес-логика и в обработчики она берется отсюда"""

from typing import List

from base import get_session
from fastapi import Depends

from sqlalchemy.orm import Session
from tables import Post


class PostService:
    def __init__(self, session: Session=Depends(get_session)):
        self.session = session

    def get_list(self) -> List[Post]:
        posts = (
        self.session.query(Post).all()
    ) 
        return posts
