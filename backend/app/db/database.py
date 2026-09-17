from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db:5432/agent_harness"


engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(
    bind = engine,
    autoflush= False,
    autocommit = False,
)

