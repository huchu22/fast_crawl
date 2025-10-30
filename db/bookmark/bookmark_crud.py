from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from db.article.article_models import Article
from db.bookmark.models import Bookmark
from datetime import datetime

def add_bookmark(db: Session, article_id: str, site_name: str):
    bookmark = Bookmark(article_id=article_id, site_name=site_name, bookmarked_at=datetime.now())
    try:
        db.add(bookmark)
        db.commit()
        return bookmark
    except IntegrityError as e:
        db.rollback() # 트렌잭션 롤백
        # 이미 존재하면 그냥 반환
        existing  = db.query(Bookmark).filter_by(article_id=article_id, site_name=site_name).first()
        return existing

def delete_bookmark(db: Session, article_id: str, site_name: str):
    bookmark = db.query(Bookmark).filter(
        Bookmark.article_id==article_id,
        Bookmark.site_name == site_name
    ).first()
    if bookmark:
        db.delete(bookmark)
        db.commit()
    return bookmark

def get_bookmarked_articles(db: Session):
    """Bookmark -> Total_articles Join -> 실제 게시글 데이터 반환"""
    bookmarks = (
        db.query(Article)
        .join(Bookmark,
              (Bookmark.article_id == Article.article_id) &
              (Bookmark.site_name == Article.siteName))
        .order_by(Bookmark.bookmarked_at.desc())
        .all()
    )
    return bookmarks