"""здесь хранятся функции обработчики запроса"""

from typing import List, Optional

from fastapi import Depends, APIRouter, Response, status
from models.posts import Post, PostKind, PostCreate, Post_update
from models.auth import User
from services.posts import PostService
from services.auth import get_current_user


router = APIRouter(
    prefix='/posts',
)


@router.get('/', response_model=List[Post])
def posts_list(
    kind: Optional[PostKind] = None,
    user: User = Depends(get_current_user),
    service: PostService = Depends(),
        ):
    return service.get_list(user_id=user.id, kind=kind)


@router.post('/', response_model=Post)
def post_create(
    post_data: PostCreate,
    user: User = Depends(get_current_user),
    service: PostService = Depends(),
        ):
    return service.create(user_id=user.id, post_data=post_data)


@router.get('/{post_id}', response_model=Post)
def get_post(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostService = Depends(),
        ):
    return service.get_one(user_id=user.id, post_id=post_id)


@router.put('/{post_id}', response_model=Post)
def post_update(
    post_id: int,
    post_data: Post_update,
    user: User = Depends(get_current_user),
    service: PostService = Depends(),
        ):
    return service.update(
        uder_id=user.id,
        post_id=post_id,
        post_data=post_data,
        )


@router.delete('/{post_id}')
def post_delete(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostService = Depends()
        ):
    service.delete(user_id=user.id, post_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
