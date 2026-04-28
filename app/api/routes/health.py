from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Doctor


router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    return {"status": "ok"}

@router.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"message": "DB connected"}

@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    return db.query(Doctor).all()