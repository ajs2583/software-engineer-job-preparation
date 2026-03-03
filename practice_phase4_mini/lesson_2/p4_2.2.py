# Query parameters
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/equipment/{serial_number}")
def root(serial_number: str) -> dict[str, str]:
    return {serial_number: "active"}


@app.get("/equipment/")
async def get_equipment(
    is_calibrated: Optional[bool] = None, limit: int = 10
) -> dict[str, bool | int | None]:
    return {"Calibrated status": is_calibrated, "limit": limit}
