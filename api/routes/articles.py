from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from db.article.schemas import Pagination, ArticleBase
from db.session import get_db
from db.article import crud
from db.article.article_models import Article

router = APIRouter()

# 게시글 전체 및 페이지네이션 불러오기
@router.get("", response_model=Pagination)
def get_articles(
        page: int = Query(1, ge=1), # page만 입력
        db: Session = Depends(get_db)
):
    """DB에 저장되어 있는 인기글 목록 반환(페이지네이션 포함)"""
    limit = 15 # limit 내부 고정(url 깔끔)
    offset = (page - 1) * limit
    return crud.get_all_articles(db, offset = offset, limit = limit)

@router.get("/sitename/{siteName}", response_model=Pagination)
def get_article_sitename(
        siteName: str,
        page: int = Query(1, ge = 1),
        db: Session = Depends(get_db),
):
    """사이트별 목록 반환 (페이지네이션 포함)"""
    limit = 15
    offset = (page - 1) * limit
    return crud.get_articles_sitename(db, siteName, offset = offset, limit = limit)