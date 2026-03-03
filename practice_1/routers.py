from fastapi import APIRouter, HTTPException
from schema import Equipment
from datetime import date

router = APIRouter()

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


@router.get("/")
async def root() -> list[Equipment]:
    return equipment_list


@router.get("/{id}")
async def equipment_id(id: int) -> Equipment:
    for item in equipment_list:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Equipment not found")


@router.post("/")
async def create_new(equipment: Equipment) -> Equipment:
    equipment_list.append(equipment)
    return equipment


@router.delete("/{id}")
async def remove_item(id: int):
    for item in equipment_list:
        if item.id == id:
            equipment_list.remove(item)
            return {"message": "Equipment deleted"}
    raise HTTPException(status_code=404, detail="Equipment could not be found/deleted")
