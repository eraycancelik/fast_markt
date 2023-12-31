from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# Format of sqlalchemy database url:
# "postgresql://<user_name>:<password>@<ip_address/hostname>:<database>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# Create a database engine
# engine is used to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         connection = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="159632159",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = connection.cursor()
#         print("Veritabanına bağlanıldı.")
#         break
#     except Exception as error:
#         print("Veritabanına bağlanılamadı.")
#         print("Hata:")
#         print(str(error))
#         time.sleep(2)
