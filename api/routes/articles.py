from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db import crud

router = APIRouter()

@router.get("/")
def get_articles(db: Session = Depends(get_db)):
    """DB에 저장되어 있는 인기글 목록 반환"""
    return crud.get_all_articles(db)

@router.get("/sitename/{siteName}")
def get_article_sitename(siteName: str, db: Session = Depends(get_db)):
    """사이트별 목록 반환"""
    return crud.get_articles_sitename(db, siteName)