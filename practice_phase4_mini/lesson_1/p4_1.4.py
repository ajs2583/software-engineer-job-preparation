# async and await
import asyncio


async def run_test(unit_name: str):
    print(f"Starting test for {unit_name}")
    await asyncio.sleep(1)
    print(f"Test complete for {unit_name}")
    return "pass"


asyncio.run(run_test(unit_name="Oscilloscope 4"))
