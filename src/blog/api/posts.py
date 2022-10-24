"""здесь хранятся функции обработчики запроса"""

from typing import List, Optional

from fastapi import Depends, APIRouter, Response, status
from models.posts import Post, PostKind, PostCreate, Post_update
from services.posts import PostService


router = APIRouter(
    prefix='/posts',
)


@router.get('/', response_model=List[Post])
def posts_list(
    kind: Optional[PostKind] = None,
    service: PostService = Depends()
        ):
    return service.get_list(kind=kind)


@router.post('/', response_model=Post)
def post_create(
    post_data: PostCreate,
    service: PostService = Depends(),
        ):
    return service.create(post_data)


@router.get('/{post_id}', response_model=Post)
def get_post(
    post_id: int,
    service: PostService = Depends(),
        ):
    return service.get_one(post_id)


@router.put('/{post_id}', response_model=Post)
def post_update(
    post_id: int,
    post_data: Post_update,
    service: PostService = Depends(),
        ):
    return service.update(post_id, post_data)


@router.delete('/{post_id}')
def post_delete(
    post_id: int,
    service: PostService = Depends()
        ):
    service.delete(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
