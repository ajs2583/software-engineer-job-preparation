from sqlalchemy import Column, Integer, String, Boolean, Date
from database import Base


class Equipment(Base):
    __tablename__ = "equipment"
    id: Column[int] = Column(Integer, primary_key=True)
    name: Column[str] = Column(String, nullable=False)
    serial_number: Column[str] = Column(String, nullable=False, unique=True, index=True)
    type: Column[str] = Column(String, nullable=False)
    is_calibrated: Column[bool] = Column(Boolean, default=False)
    last_calibrated: Column[Date] = Column(Date, nullable=True)
