"""здесь хранится бизнес-логика и в обработчики она берется отсюда"""

from typing import List, Optional

from base import get_session
from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session
from models.posts import PostKind, PostCreate, Post_update
from tables import Post


class PostService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_one(self, user_id: int, post_id: int) -> Post:
        post = (
            self.session
            .query(Post)
            .filter_by(id=post_id, user_id=user_id)
            .first()
        )
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get_list(
        self,
        user_id: int,
        kind: Optional[PostKind] = None,
            ) -> List[Post]:
        query = (
            self.session.query(Post)
            .filter_by(user_id=user_id)
            )
        if kind:
            query = query.filter_by(kind=kind)
        posts = query.all()
        return posts

    def get_one(self, user_id: int, post_id: int) -> Post:
        return self._get_one(user_id, post_id)

    def create(self, user_id: int, post_data: PostCreate) -> Post:
        post = Post(
            **post_data.dict(),
            user_id=user_id,
                )
        self.session.add(post)
        self.session.commit()
        return post

    def update(
        self,
        user_id: int,
        post_id: int,
        post_data: Post_update,
            ) -> Post:
        post = self._get_one(user_id, post_id)
        for field, value in post_data:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delete(self, user_id: int, post_id: int):
        post = self._get_one(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
