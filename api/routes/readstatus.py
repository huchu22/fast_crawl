from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from db.session import get_db
from db.read_status import read_status_curd

router = APIRouter()

@router.post("")
def add_readstatus(
        site_name: str = Query(...),
        article_id: str = Query(...),
        db: Session = Depends(get_db),
):
    return read_status_curd.add_readStatus(db,article_id, site_name)

@router.get("")
def get_readstatus(db: Session = Depends(get_db),
):
    return read_status_curd.get_readStatus(db)
