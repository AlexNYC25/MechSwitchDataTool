from pymongo import MongoClient
from dotenv import load_dotenv
import pprint
import os

load_dotenv()

class mechanicalClient:
    def __init__(self):
        self.client = MongoClient(os.environ.get('MONGO_URI'))
        self.db = self.client.Mechanical_switches

        self.switches = self.db.switches
    
    def getSwitch(self, switch_id):
        return self.switches.find_one({"_id": switch_id})

    def getAllSwitches(self):
        return self.switches.find()

    def insertSwitch(self, switch):
        self.switches.insert_one(switch)

    def updateSwitch(self, switch_id, switch):
        self.switches.update_one({"_id": switch_id}, {"$set": switch})

    def deleteSwitch(self, switch_id):
        self.switches.delete_one({"_id": switch_id})