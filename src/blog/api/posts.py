"""здесь хранятся функции обработчики запроса"""

from typing import List

from fastapi import Depends
from fastapi import APIRouter
from models.posts import Post
from services.posts import PostService



router = APIRouter( 
prefix='/posts',
)

@router.get('/', response_model=List[Post])
def posts_list(service: PostService=Depends()):
    return service.get_list()
