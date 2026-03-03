from pydantic import BaseModel
from fastapi import FastAPI


class EquipmentResponse(BaseModel):
    serial_number: str
    type: str
    is_calibrated: bool


app = FastAPI()


@app.get("/equipment/{serial_number}", response_model=EquipmentResponse)
def root(serial_number: str) -> EquipmentResponse:
    return {
        "serial_number": serial_number,
        "type": "stuff",
        "is_calibrated": True,
        "internal notes": "notes",
    }
