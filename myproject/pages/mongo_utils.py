import pymongo
from django.conf import settings

def get_mongo_client():
    mongo_client = pymongo.MongoClient(host=settings.MONGO_HOST, port=settings.MONGO_PORT)
    return mongo_client
