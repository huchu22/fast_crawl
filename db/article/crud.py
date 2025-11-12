from sqlalchemy.orm import Session

from db.article.article_models import Article

def get_all_articles(db, offset=0, limit=20):
    query = db.query(Article).filter(Article.siteName != 'hot_deal')
    total = db.query(Article).count()
    items = (
        query
         .order_by(Article.creationDate.desc())
         .offset(offset)
         .limit(limit)
         .all()
     )
    return {"total": total, "page": offset // limit + 1, "items": items}

def get_articles_sitename(
        db: Session,
        siteName: str,
        offset: int = 0,
        limit: int = 15
):
    total = db.query(Article).filter(Article.siteName == siteName).count()
    items = (
        db.query(Article)
        .filter(Article.siteName == siteName)
        .order_by(Article.creationDate.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
    return {"total": total, "page": offset // limit + 1, "items": items}
