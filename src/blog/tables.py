import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DATE)
    text = sa.Column(sa.Text, nullable=False)
    kind = sa.Column(sa.String)
    

