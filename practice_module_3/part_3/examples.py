from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base


# Create database connection
engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)
db = Session()


class TestRun(Base):
    __tablename__ = "test_runs"
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey("units.id"))
    started_at = Column(DateTime, nullable=True)


class Unit(Base):
    __tablename__ = "unit"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)


"""
# Get all records
db.query(Unit).all()

# Get first match
db.query(Unit).first()

# Filter by a field
db.query(Unit).filter(Unit.name == "Oscilloscope A").first()

# Filter by multiple conditions
db.query(Unit).filter(Unit.is_active, Unit.name == "Oscilloscope A").all()

# Filter by foreign key
db.query(TestRun).filter(TestRun.unit_id == 1).all()

"""

db.query(Unit).all()

db.query(TestRun).filter(TestRun.id == 1).first()

db.query(TestRun).filter(TestRun.unit_id == 3).all()

db.query(Unit).filter(Unit.serial_number == "OSC-001").first()
