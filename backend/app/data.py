from fastapi import HTTPException
import pymongo
from bson.objectid import ObjectId
import os
import app.schemas as schemas
from datetime import datetime, timezone
from app.idhash import IdHash

class Data():

  def connect():
    conn = os.environ['MONGO_CONNECT']
    client = pymongo.MongoClient(conn)
    db = client.db1
    col = db["docs"]
    return col

  def getDoc(doc_id):
    col = Data.connect()
    res = col.find_one({"_id": doc_id}, {'_id': 0})
    print(res)
    if res != None:
      return res
    raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")
  
  def createDoc(doc):
    # TODO: handle case id already exists 
    id = IdHash.hash()
    col = Data.connect()
    d = {'_id': id, 'Time': datetime.now(timezone.utc), 'Doc': doc.doc}
    res = col.insert_one(d)
    return res.inserted_id