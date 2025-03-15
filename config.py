
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:1415@localhost:5432/bond_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
