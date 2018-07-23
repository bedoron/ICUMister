import os
from _ssl import CERT_NONE
import pymongo as pymongo

MONGO_URI = "mongodb://%s:%s@%s.documents.azure.com:10255/?ssl=true&replicaSet=globaldb" % (
    os.environ['DBNAME'], os.environ['DBPASS'], os.environ['DBNAME'])

KNOWN_PERSON_GROUP = "HackathonPersonGroup"
UNKNOWN_PERSON_GROUP = "UnknownHackathonPersonGroup"
IGNORE_PERSON_GROUP = "IgnoreHackathonPersonGroup"


def get_db():
    """
    :rtype:  Database
    """
    client = pymongo.MongoClient(MONGO_URI, ssl_cert_reqs=CERT_NONE)
    return client.get_database('icumister')
