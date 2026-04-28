from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialty = Column(String, index=True)
    experience = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    rating = Column(Float)
    city = Column(String)