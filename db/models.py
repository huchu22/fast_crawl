from sqlalchemy import Column, String, DateTime, func
from db.session import Base

class Article(Base):
    __tablename__ = "total_articles"

    article_id = Column(String, primary_key=True)
    title = Column(String(255))
    creationDate = Column("creation_date", DateTime)
    siteUrl = Column("article_url", String(2048))
    siteName = Column("site_name", String(255), primary_key=True)
    collected_date = Column(DateTime, default=func.now())
