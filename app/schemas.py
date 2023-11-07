from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from pydantic.types import conint
# Her Post işleminde status_code=201 ile 201 kodu döndürülür.
# BaseModel: Pydantic kütüphanesinden gelen bir sınıf. Pydantic, veri doğrulama ve serielleştirme için kullanılır.
# BaseModel sınıfından türetilen sınıflar, Pydantic tarafından otomatik olarak doğrulanır ve serielleştirilir.
# Pydantic, veri doğrulama ve serielleştirme için kullanılır.

# Users tablosu için kullanılacak olan sınıflar.
class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    phone: int

    class Config:
        orm_mode = True

class UserDetail(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: int
    admin: bool
    created_at: datetime

    class Config:
        orm_mode = True

class UserInfo(BaseModel):
    name: str
    surname: str
    email: EmailStr
    phone: int

    class Config:
        orm_mode = True




class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Post tablosu için kullanılacak olan sınıflar.
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass
class UserOut(BaseModel):
    user_id: int
    name: str
    surname: str
    email: EmailStr
    phone: int
    created_at: datetime

    class Config:
        orm_mode = True
class Post(PostBase):
    post_id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

# Products tablosu için kullanılacak olan sınıflar.
class ProductBase(BaseModel):
    product_name: str
    product_price: float
    product_photo_url: str
    product_category: str


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Token için kullanılacak olan sınıflar.
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir:conint(le=1)

class AddressBase(BaseModel):
    address_type: str
    address_user_name: str
    address_user_surname: str
    address_user_phone: str
    address_city: str
    address_line: str
    zipcode: int

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    address_id: int
    customer_id: int
    customer: UserOut
    class Config:
        orm_mode = True

class UserList(BaseModel):
    user_list: List[UserOut]
class UserInf(BaseModel):
    user: UserOut
