from pymongo import MongoClient


def db():
    client = MongoClient("mongodb://42.114.245.120:27098")

    db = client['push']
    cpumem = db['cpumem']
    return cpumem


print(db())
# job = 'dev'

# Dev-Staging-245-120
# import datetime
# Dev_Staging_245_120 = [
#     datetime.datetime.now(), '30', '30'
# ]
# cpumem.update_many({}, {"$push": {"Dev-Staging-245-120": Dev_Staging_245_120}})

# import pprint
# for doc in cpumem.find({'job': job}):
#     pprint.pprint(doc)
