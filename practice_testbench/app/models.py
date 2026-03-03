# SQLAlchemy ORM models
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey


class Base(DeclarativeBase):
    pass


class Units(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True)
    serial_number = Column(String, unique=True)
    product_type = Column(String)
    manufacture_date = Column(DateTime)

    test_results = relationship("TestResults", back_populates="units")


class TestResults(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    unit_id = Column(Integer, ForeignKey("units.id"))
    has_passed = Column(Boolean)
    timestamp = Column(DateTime)
    notes = Column(String, nullable=True)

    units = relationship("Units", back_populates="test_results")
