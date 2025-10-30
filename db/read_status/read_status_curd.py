from sqlalchemy.orm import Session
from sqlalchemy import and_
from db.article.article_models import Article
from db.read_status.models import ReadStatus

def add_readStatus(db: Session, article_id: str, site_name: str):
    readStatus = ReadStatus(article_id=article_id, site_name=site_name)
    try:
        db.add(readStatus)
        db.commit()
        db.refresh(readStatus)
        return readStatus
    except Exception:
        db.rollback()
        existing = (
            db.query(ReadStatus)
            .filter(ReadStatus.article_id == article_id, ReadStatus.site_name == site_name)
            .first()
        )
        return existing

def get_readStatus(db: Session):
    readStatus = (
        db.query(Article)
        .join(ReadStatus,
              (ReadStatus.article_id == Article.article_id) &
              (ReadStatus.site_name == Article.siteName))
        .all()
    )
    return readStatus
