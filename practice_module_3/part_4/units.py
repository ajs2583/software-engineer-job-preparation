from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database import Base


class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    test_runs = relationship("TestRun", back_populates="unit")
