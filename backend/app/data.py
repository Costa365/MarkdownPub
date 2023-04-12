import os
from datetime import datetime, timezone

import pymongo
from app.idhash import IdHash
from fastapi import HTTPException


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
        print(res)
        if res is not None:
            return res
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")

    def createDoc(self, doc):
        # TODO: handle case id already exists
        idHash = IdHash()
        id = idHash.hash()
        d = {"_id": id, "Time": datetime.now(timezone.utc), "Doc": doc.doc}
        res = self.col.insert_one(d)
        return res.inserted_id
