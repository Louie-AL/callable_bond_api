from sqlalchemy import Column, Integer, Float, String
from backend.database import Base

class BondPriceResult(Base):
    __tablename__ = "bond_prices"

    id = Column(Integer, primary_key=True, index=True)
    bond_type = Column(String, index=True)
    initial_price = Column(Float)
    strike_price = Column(Float)
    conversion_ratio = Column(Float)
    call_price = Column(Float)
    maturity = Column(Float)
    yield_to_maturity = Column(Float)
    computed_price = Column(Float)
