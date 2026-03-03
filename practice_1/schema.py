# Pydantic basemodel
from pydantic import BaseModel
from typing import Optional
from datetime import date


class Equipment(BaseModel):
    id: int
    name: str
    serial_number: str
    type: str
    is_calibrated: bool = False
    last_calibrated: Optional[date] = None
