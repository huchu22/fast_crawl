from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from db.schemas import ArticleBase, Pagination
from db.session import get_db
from db import crud

router = APIRouter()

@router.get("", response_model=Pagination)
def get_articles(
        page: int = Query(1, ge=1), # page만 입력
        db: Session = Depends(get_db)
):
    """DB에 저장되어 있는 인기글 목록 반환(페이지네이션 포함)"""
    limit = 10 # limit 내부 고정(url 깔끔)
    offset = (page - 1) * limit
    return crud.get_all_articles(db, offset = offset, limit = limit)

@router.get("/sitename/{siteName}", response_model=Pagination)
def get_article_sitename(
        siteName: str,
        page: int = Query(1, ge = 1),
        db: Session = Depends(get_db),
):
    """사이트별 목록 반환 (페이지네이션 포함)"""
    limit = 10
    offset = (page - 1) * limit
    return crud.get_articles_sitename(db, siteName, offset = offset, limit = limit)