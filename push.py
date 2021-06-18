import detail_cpu_memory as dtcpumem
import connect_mongodb as mongodb
import time


while True:

    cpu, mem = dtcpumem.detailCpu_Mem()

    import datetime

    Dev_Staging_245_120 = [
        datetime.datetime.now(), cpu, mem
    ]
    mongodb.db().update_many({}, {"$push": {"Dev-Staging-245-120": Dev_Staging_245_120}})
    time.sleep(60)
