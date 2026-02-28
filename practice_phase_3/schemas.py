from pydantic import ConfigDict
from pydantic import BaseModel
from typing import Optional
from datetime import date


# Pydantic BaseModel
class EquipmentCreate(BaseModel):
    name: str
    serial_number: str
    type: str
    is_calibrated: bool = False
    last_calibrated: Optional[date] = None


class EquipmentResponse(EquipmentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
