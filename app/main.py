import time
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

import routers.auth as auth_router
import routers.products as products_router
import routers.users as users_router

import database,models

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

while True:
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="159632159",
            cursor_factory=RealDictCursor,
        )
        cursor = connection.cursor()
        print("Veritabanına bağlanıldı.")
        break
    except Exception as error:
        print("Veritabanına bağlanılamadı.")
        print("Hata:")
        print(str(error))
        time.sleep(2)

app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(users_router.router)


@app.get("/")
def say_hi():
    return {"message": "server is running"}