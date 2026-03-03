# Routers
from fastapi import FastAPI
from p4_equipment import equipment

app = FastAPI()
app.include_router(equipment.router)
