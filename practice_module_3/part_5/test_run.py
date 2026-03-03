from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base


class TestRun(Base):
    __tablename__ = "test_runs"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey("units.id"))
    started_at = Column(DateTime, nullable=True)
    unit = relationship("Unit", back_populates="test_runs")
