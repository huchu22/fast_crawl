from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from db.session import Base

class Bookmark(Base):
    __tablename__ = 'bookmark'

    article_id = Column(String(255),
                        ForeignKey("total_articles.article_id"),
                        primary_key=True)
    site_name = Column(String(255),
                       ForeignKey("total_articles.site_name"),
                       primary_key=True)
    bookmarked_at = Column(DateTime, nullable=False)