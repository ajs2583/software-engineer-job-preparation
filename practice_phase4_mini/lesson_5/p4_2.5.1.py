from fastapi import APIRouter

router = APIRouter()


@router.get("/equipment/{serial_number}")
def root(serial_number: str) -> dict[str, str]:
    return {serial_number: "active"}
