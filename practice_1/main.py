from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()


# Pydantic basemodel
class Equipment(BaseModel):
    id: int
    name: str
    serial_number: str
    type: str
    is_calibrated: bool = False
    last_calibrated: Optional[date] = None


equipment_list: list[Equipment] = [
    Equipment(
        id=1,
        name="Oscilloscope A",
        serial_number="OSC-001",
        type="Oscilloscope",
        is_calibrated=True,
        last_calibrated=date(2024, 11, 1),
    ),
    Equipment(
        id=2,
        name="Multimeter B",
        serial_number="MM-002",
        type="Multimeter",
        is_calibrated=False,
    ),
    Equipment(
        id=3,
        name="Power Supply C",
        serial_number="PS-003",
        type="Signal Generator",
        is_calibrated=True,
        last_calibrated=date(2025, 1, 15),
    ),
]


@app.get("/equipment")
async def root() -> list[Equipment]:
    return equipment_list


@app.get("/equipment/{id}")
async def equipment_id(id: int) -> Equipment:
    for item in equipment_list:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Equipment not found")


@app.post("/equipment/")
async def create_new(equipment: Equipment) -> Equipment:
    equipment_list.append(equipment)
    return equipment


@app.delete("/equipment/{id}")
async def remove_item(id: int):
    for item in equipment_list:
        if item.id == id:
            equipment_list.remove(item)
            return {"message": "Equipment deleted"}
    raise HTTPException(status_code=404, detail="Equipment could not be found/deleted")
