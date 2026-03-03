# Pydantic request/response schemas
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class UnitBase(BaseModel):
    serial_number: str
    product_type: str
    manufacture_date: datetime


class UnitCreateRequest(UnitBase):
    pass


class UnitResponse(UnitBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TestResultBase(BaseModel):
    test_name: str
    unit_id: int
    has_passed: bool

    notes: Optional[str] = None


class TestResultCreateRequest(TestResultBase):
    pass


class TestResultResponse(TestResultBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    timestamp: datetime
