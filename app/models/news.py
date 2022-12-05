from sqlalchemy import Column, String

from app.core.db import Base

class News(Base):
    title = Column(String(100), unique=False, nullable=True)
    url = Column(String(100), unique=False, nullable=True)
    news_date = Column(String(100), unique=False, nullable=True)

    def __repr__(self):
        return f'id: {self.id}, title: {self.title}, url: {self.url}, ' \
               f'news_date: {self.news_date}'