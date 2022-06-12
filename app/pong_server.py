import asyncio
import os
from datetime import datetime

import requests
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

other_service_address = os.getenv('OTHER_SERVICE_ADDRESS', 'http://www.google.com')
pong_time_ms = float(os.getenv('PONG_TIME_MS', '3000'))


async def log(response: requests.Response):
    print(f"received pong at {datetime.now()}")
    print(f"pinged {other_service_address} after {pong_time_ms}ms")
    print(f"response from {other_service_address}: {response.text}")


async def wait_and_ping_other():
    await asyncio.sleep(pong_time_ms / 1000.0)
    log(requests.get(other_service_address + "/ping"))


@app.get("/ping")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(wait_and_ping_other)
    return "pong"
