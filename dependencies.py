from sqlalchemy.orm import sessionmaker
from models import engine
# from security import 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def getSession():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()