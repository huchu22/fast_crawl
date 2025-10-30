from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.bookmark.schemas import Bookmark
from db.session import get_db
from db.bookmark import bookmark_crud

router = APIRouter()

@router.post("")
def add_bookmark(
        site_name: str = Query(...),
        article_id: str = Query(...),
        db: Session = Depends(get_db)
):
    return bookmark_crud.add_bookmark(db, article_id, site_name)

@router.delete("")
def delete_bookmark(
        site_name: str = Query(...),
        article_id: str = Query(...),
        db: Session = Depends(get_db)
):
    deleted = bookmark_crud.delete_bookmark(db, article_id, site_name)
    if not deleted:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return {"detail": "Bookmark deleted"}

@router.get("")
def get_all_bookmarks(db: Session = Depends(get_db)):
    return bookmark_crud.get_bookmarked_articles(db)