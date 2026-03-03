from  import null
from database import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship


class TestResults(Base):
    __tablename__ = "test_results"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey("test_results.id"))
    is_successful = Column(Boolean)
    ended_at = Column(DateTime, nullable=True)
    test_name = (String)
    created_at = Column(DateTime, nullable=True)
    failre_reason = Column(String, nullable=True)
    test_run = relationship("test_run", back_populates="test_results")
    created_at = 
