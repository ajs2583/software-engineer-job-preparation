from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from database import Base


class TestRun(Base):
    __tablename__ = "test_runs"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey("units.id"))
    started_at = Column(DateTime, nullable=True)
    unit = relationship("Unit", back_populates="test_runs")


class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    test_runs = relationship("TestRun", back_populates="unit")


# Create database connection
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
db = Session()

# 1
db.query(TestRun).join(Unit, TestRun.unit_id == Unit.id).all()

# 2
db.query(TestRun).join(Unit).filter(Unit.serial_number == "OSC-001").all()

# 3
db.query(TestRun).join(Unit).filter(TestRun.started_at != None).all()
