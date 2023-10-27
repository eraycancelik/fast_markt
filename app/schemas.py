from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Her Post işleminde status_code=201 ile 201 kodu döndürülür.
# BaseModel: Pydantic kütüphanesinden gelen bir sınıf. Pydantic, veri doğrulama ve serielleştirme için kullanılır.
# BaseModel sınıfından türetilen sınıflar, Pydantic tarafından otomatik olarak doğrulanır ve serielleştirilir.
# Pydantic, veri doğrulama ve serielleştirme için kullanılır.


class ProductBase(BaseModel):
    product_name: str
    product_price: float
    product_photo_url: str
    product_category: str


class ProductCreate(ProductBase):
    is_sale: Optional[bool] = True
    pass


# çağırıldığında response un içeriğini bu şekilde döndürür.
class Product(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    phone: int
    admin: Optional[bool] = False

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: int

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    user_id: int
    name: str
    surname: str
    email: EmailStr
    phone: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
