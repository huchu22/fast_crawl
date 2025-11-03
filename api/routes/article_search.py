from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Query
from db.session import get_db
from db.article.article_models import Article

router = APIRouter()

# 검색 로직 추가
@router.get("")
def search_articles(
        keyword: str = Query(..., description= "검색을 위한 단어"),
        db: Session = Depends(get_db),
):
    result = (
        db.query(Article)
        .filter(Article.title.ilike(f"%{keyword}%"))
        .order_by(Article.creationDate.desc())
        .all()
    )
    return result