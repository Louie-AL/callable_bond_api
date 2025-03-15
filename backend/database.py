from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1415@localhost:5432/callable_bond_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Ensure models are imported before creating tables
    from backend.models import Base
    Base.metadata.create_all(bind=engine)

# Call init_db() inside main application entry point instead
