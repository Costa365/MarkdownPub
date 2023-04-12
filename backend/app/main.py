import app.schemas as schemas
from app.data import Data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
data = Data()

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
    return {"message": "MD-Pub API"}


@app.get("/doc/{doc_id}")
async def read_doc(doc_id):
    result = data.getDoc(doc_id)
    return {"doc": result["Doc"]}


@app.post("/doc")
async def create_doc(md: schemas.MarkDown):
    id = data.createDoc(md)
    return {"doc": str(id)}
