from typing import Optional


# Extend to accept optional
def describe_equipment(
    name: str,
    serial_number: str,
    is_callibrated: bool,
    last_calibrated: Optional[str] = None,
) -> str:
    if last_calibrated:
        return f"{name} ({serial_number}) - Calibrated: {is_callibrated} - Last Calibration: {last_calibrated}"
    else:
        return f"{name} ({serial_number}) - Last Calibration: Never"
