import asyncio
import os

import requests
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

other_service_address = os.getenv('OTHER_SERVICE_ADDRESS', 'http://www.google.com')
pong_time_ms = float(os.getenv('PONG_TIME_MS', '3000'))


async def wait_and_ping_other():
    await asyncio.sleep(pong_time_ms / 1000.0)
    response = requests.get(other_service_address + "/ping")
    print(f"pinged {other_service_address} after {pong_time_ms} ms.\nresponse was: {response}")


@app.get("/ping")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(wait_and_ping_other)
    return "pong"
