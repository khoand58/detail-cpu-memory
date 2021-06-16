import uvicorn
from fastapi import FastAPI
import detail_cpu_memory as dt
from pydantic import BaseModel

import time

# from datetime import datetime, time, timedelta
#
app = FastAPI()


class Detailcpumemory(BaseModel):
    Duration: int


@app.get("/detail_cpu_memory1/")
def detail_cpu_memory1():
    status = 'Nomarl'
    cpu, mem = dt.detailCpu_Mem()
    print(cpu)
    print(mem)
    if cpu > 80.0 or mem > 80.0:
        status = 'Critical'
    elif cpu > 70.0 or mem > 70.0:
        status = 'Warning'
    return {
        "status": status,
    }


@app.post("/detail_cpu_memory2/")
async def detail_cpu_memory2(detailcpumemory: Detailcpumemory):
    status = 'Nomarl'
    cpu1, mem1 = dt.detailCpu_Mem()
    print(cpu1)
    print(mem1)
    time.sleep(detailcpumemory.Duration * 60)
    cpu2, mem2 = dt.detailCpu_Mem()
    print(cpu2)
    print(mem2)
    if (cpu2 - cpu1) > 30.0 or (mem2 - mem1) > 30.0:
        status = 'Critical'
    print(detailcpumemory)
    return {
        "status": status,
        "Duration": detailcpumemory.Duration,
    }
