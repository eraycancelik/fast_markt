from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, oauth2
from database import get_db
from sqlalchemy import func

router = APIRouter(
    prefix="/addresses",
    tags=["Address"],
    responses={404: {"description": "Not found"}},
)
@router.get("/", response_model=List[schemas.Address])
def get_addresses(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.name, current_user.surname)
    addresses = db.query(models.Address).all()
    return addresses