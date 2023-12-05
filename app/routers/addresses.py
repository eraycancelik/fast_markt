from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/address",
    tags=["Address"],
    responses={404: {"description": "Not found"}},
)
@router.get("/", response_model=List[schemas.Address])
def get_addresses(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    addresses = db.query(models.Address,).filter(models.Address.customer_id == current_user.user_id).all()
    return addresses

@router.post("/", response_model=schemas.Address, status_code=status.HTTP_201_CREATED)
def create_address(address:schemas.AddressCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_address=models.Address(customer_id=current_user.user_id,**dict(address))
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address
