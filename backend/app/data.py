import os
from datetime import datetime, timezone

import pymongo
from app.idhash import IdHash


class Data:
    def __init__(self):
        self.col = self.__connect()

    def __connect(self):
        conn = os.environ["MONGO_CONNECT"]
        client = pymongo.MongoClient(conn)
        db = client.db1
        col = db["docs"]
        return col

    def getDoc(self, doc_id):
        res = self.col.find_one({"_id": doc_id}, {"_id": 0})
        return res

    def createDoc(self, doc):
        # TODO: handle case id already exists
        idHash = IdHash()
        id = idHash.hash()
        editId = idHash.hash()
        d = {
            "_id": id,
            "Time": datetime.now(timezone.utc),
            "Doc": doc.doc,
            "EditId": editId,
        }
        res = self.col.insert_one(d)
        return [res.inserted_id, editId]

    def updateDoc(self, doc):
        d = {
            "Time": datetime.now(timezone.utc),
            "Doc": doc.doc,
        }

        query = {"EditId": doc.editId}
        newvalues = {"$set": d}
        res = self.col.update_one(query, newvalues)
        return res.modified_count > 0
