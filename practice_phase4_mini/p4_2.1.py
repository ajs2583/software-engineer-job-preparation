# Path parameters
from fastapi import FastAPI

app = FastAPI()


@app.get("/equipment/{serial_number}")
def root(serial_number: str) -> dict[str, str]:
    return {serial_number: "active"}
