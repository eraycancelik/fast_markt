from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database, oauth2

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.Product])
def get_sqlalchemy(db: Session = Depends(database.get_db)):
    products = db.query(models.Products).all()
    return products


@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    product = (
        db.query(models.Products)
        .filter(models.Products.product_id == product_id)
        .first()
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id:{product_id} was not found",
        )
    return product


# Her Post işleminde status_code=201 ile 201 kodu döndürülür.
# response_model=schemas.Product ile response un içeriğini "Product"ın içeriği şekilde döndürür.
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    if current_user.admin == False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with id:{current_user.user_id} is not authorized to create a product",
        )
    new_product = models.Products(**dict(product))
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    print(current_user)
    if current_user.admin == False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with id:{current_user.user_id} is not authorized to delete this product",
        )
    product = (
        db.query(models.Products)
        .filter(models.Products.product_id == product_id)
        .first()
    )
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id:{product_id} was not found",
        )
    db.delete(product)
    db.commit()
    return {"data": "Product deleted successfully"}


@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int,
    updated_product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    if current_user.admin == False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"User with id:{current_user.user_id} is not authorized to update this product",
        )
    product_query = db.query(models.Products).filter(
        models.Products.product_id == product_id
    )
    product = product_query.first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id:{product_id} was not found",
        )
    product_query.update(dict(updated_product), synchronize_session=False)
    db.commit()
    db.refresh(product)
    return product
