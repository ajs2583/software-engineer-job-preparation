from database import engine
from database import Base
from models import Equipment
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import EquipmentCreate, EquipmentResponse
from database import get_db


app = FastAPI()


Base.metadata.create_all(bind=engine)


# returns equipment list
@app.get("/equipment")
async def get_equipment(db: Session = Depends(get_db)):
    equipment_list = db.query(Equipment).all()
    return equipment_list


@app.post("/equipment", response_model=EquipmentResponse)
async def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    db_equipment = Equipment(
        name=equipment.name,
        serial_number=equipment.serial_number,
        type=equipment.type,
        is_calibrated=equipment.is_calibrated,
        last_calibrated=equipment.last_calibrated,
    )
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment


# get id
@app.get("/equipment/{equipment_id}", response_model=EquipmentResponse)
async def get_equipment_by_id(equipment_id: int, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment


# delete
@app.delete("/equipment/{equipment_id}")
async def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    db.delete(equipment)
    db.commit()
    return {"detail": "Equipment deleted successfully"}
