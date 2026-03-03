from fastapi import FastAPI
from routers import equipment

app = FastAPI()


app.include_router(equipment.router, prefix="/equipment", tags=["equipment"])
