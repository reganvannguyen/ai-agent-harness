from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:mysecretpassword@localhost:5432/agent_harness"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush= False,
    autocommit = False,
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        