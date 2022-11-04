from io import StringIO
from typing import Any
import csv
from fastapi import Depends

from services.posts import PostService
from models.posts import PostCreate, Post


class ReportServce:
    def __init__(self, post_service: PostService = Depends()):
        self.post_service = post_service

    def import_csv(self, user_id: int, file: Any):
        reader = csv.DictReader(
            (line.decode() for line in file),
            fieldnames=[
                'date',
                'text',
                'kind',
            ],
        )

        posts = []
        for item in reader:
            post_data = PostCreate.parse_obj(item)
            if post_data.text == '':
                post_data.text = None
            posts.append(post_data)

        self.post_service.create_many(
            user_id,
            posts
        )

    def export_csv(self, user_id: int) -> Any:
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=[
                'date',
                'text',
                'kind',
            ],
            extrasaction='ignore',
        )

        posts = self.post_service.get_list(user_id)

        writer.writeheader()
        for post in posts: 
            post_data = Post.from_orm(post)
            writer.writerow(post_data.dict())

        output.seek(0)
        return output


