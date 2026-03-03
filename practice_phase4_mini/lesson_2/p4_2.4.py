# Depends and Depedency Injection
from fastapi import Depends, FastAPI

app = FastAPI()


def get_test_config():
    return {"max_results": 100, "enviroment": "development"}


@app.get("/config")
async def get_tests(settings: dict = Depends(get_test_config)):
    return settings
