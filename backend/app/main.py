import app.schemas as schemas
from app.data import Data
from fastapi import FastAPI, HTTPException
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
    if result is not None:
        return {"doc": result["Doc"]}
    else:
        raise HTTPException(status_code=404, detail=f"Document {doc_id} not found")


@app.post("/doc")
async def create_doc(md: schemas.MarkDown):
    [id, eid] = data.createDoc(md)
    return {"doc": str(id), "editId": str(eid)}


@app.put("/doc")
async def update_doc(emd: schemas.MarkDownUpdate):
    result = data.updateDoc(emd)
    if result:
        return {"status": "success"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
