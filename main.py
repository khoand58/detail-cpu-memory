import uvicorn
from fastapi import FastAPI
import detail_cpu_memory as dt
from pydantic import BaseModel
import connect_mongodb as mongodb
import pprint
import time
import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

# from datetime import datetime, time, timedelta
#
app = FastAPI()


class Detailcpumemory(BaseModel):
    Duration: int


@app.get("/detail_cpu_memory1/{job}")
def detail_cpu_memory1(job: str):
    global list_host
    query = {"job": job}
    result = []
    dtime = datetime.datetime.now()
    dtime = dtime + datetime.timedelta(minutes=-1)
    dtime = dtime.strftime("%Y-%m-%d %H:%M")
    print(dtime)
    # get list host
    # =================
    data = mongodb.db().find(query)
    for i in data:
        list_host = i['list_host']
    # ==================

    # get date time get cpu mem
    # =============================
    for host in list_host:
        data = mongodb.db().find(query)
        for i in data:
            for h in reversed(i[host]):
                if h["date_push"] == dtime:
                    if h["cpu"] >= 70 or h["mem"] >= 70:
                        status = "Warning"
                        tmp = [host, status]
                        result.append(tmp)
                    elif h["cpu"] >= 80 or h["mem"] >= 80:
                        status = "Critical"
                        tmp = [host, status]
                        result.append(tmp)
                    else:
                        status = "OK"
                        tmp = [host, status]
                        result.append(tmp)
    # ======================================
    return {
        "result": result,
    }


@app.post("/detail_cpu_memory2/{job}")
async def detail_cpu_memory2(job: str, detailcpumemory: Detailcpumemory):
    global list_host
    query = {"job": job}
    result = []
    status = 'OK'
    dtimeEnd = datetime.datetime.now()
    dtimeEnd = dtimeEnd + datetime.timedelta(minutes=-1)
    dtimeEnd = dtimeEnd.strftime("%Y-%m-%d %H:%M")
    dtimeStart = datetime.datetime.now()
    dtimeStart = dtimeStart + datetime.timedelta(minutes=-int(detailcpumemory.Duration))
    dtimeStart = dtimeStart.strftime("%Y-%m-%d %H:%M")
    # get list host
    # =================
    data = mongodb.db().find(query)
    for i in data:
        list_host = i['list_host']
    # get date time get cpu mem
    # =============================
    for host in list_host:
        data = mongodb.db().find(query)
        for i in data:
            for h in reversed(i[host]):
                if h["date_push"] == dtimeEnd:
                    cpu2 = h["cpu"]
                    mem2 = h["mem"]
                    for h1 in reversed(i[host]):
                        if h1["date_push"] == dtimeStart:
                            cpu1 = h1["cpu"]
                            mem1 = h1["mem"]
                            # print(h["date_push"])
                            if (cpu2 - cpu1) >= 10 or (mem2 - mem1) >= 10:
                                status = "Warning"
                                tmp = {host, status}
                                result.append(tmp)
                            elif (cpu2 - cpu1) >= 30 or (mem2 - mem1) >= 30:
                                status = "Critical"
                                tmp = {host, status}
                                result.append(tmp)
                            else:
                                status = "OK"
                                tmp = {host, status}
                                result.append(tmp)
    # ======================================
    return {
        "result": result,
    }
