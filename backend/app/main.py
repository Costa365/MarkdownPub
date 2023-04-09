from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import Data
import app.schemas as schemas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {'message': 'MD-Pub API'}

@app.get("/doc/{doc_id}")
async def read_doc(doc_id):
    data = Data.getDoc(doc_id)
    return {'doc': data['Doc']}

@app.post("/doc")
async def create_doc(md:schemas.MarkDown):
    id = Data.createDoc(md)
    return {'doc': str(id)}
