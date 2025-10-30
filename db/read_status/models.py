from sqlalchemy import Column, String, DateTime, ForeignKey
from db.session import Base

class ReadStatus(Base):
    __tablename__ = 'article_read_status'

    article_id = Column(
        String,
        ForeignKey('total_articles.article_id'),
        primary_key=True
    )
    site_name = Column(
        String,
        ForeignKey('total_articles.site_name'),
        primary_key=True
    )
