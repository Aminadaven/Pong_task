import asyncio
import os
from datetime import datetime

import requests
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

other_service_address = os.getenv('OTHER_SERVICE_ADDRESS', 'http://www.google.com')
pong_time_ms = float(os.getenv('PONG_TIME_MS', '3000'))


async def log_to_file(response: requests.Response):
    with open('pong_server.log', 'a') as f:
        f.write(f"received ping at {datetime.now()}\n")
        f.write(f"pinged {other_service_address} after {pong_time_ms} ms.\n")
        f.write(f"response was: {response}\n")


async def wait_and_ping_other():
    await asyncio.sleep(pong_time_ms / 1000.0)
    log_to_file(requests.get(other_service_address + "/ping"))


@app.get("/ping")
async def ping(background_tasks: BackgroundTasks):
    background_tasks.add_task(wait_and_ping_other)
    return "pong"
