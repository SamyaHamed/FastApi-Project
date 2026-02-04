from sqlalchemy  import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "careerly.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"



engine = create_engine(DATABASE_URL,echo=True)
session_local = sessionmaker(bind= engine,autoflush= False, autocommit=False)

class Base(DeclarativeBase):
    pass



def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()