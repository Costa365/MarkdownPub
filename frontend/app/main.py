import app.schemas as schemas
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/doc/{id}", response_class=HTMLResponse)
async def get_doc(request: Request, id: str):
    r = requests.get(url="http://backend:8000/doc/" + id)
    j = r.json()
    m = j["doc"]
    return templates.TemplateResponse("doc.html", {"request": request, "markdown": m})


@app.get("/edit/{id}/{eid}", response_class=HTMLResponse)
async def edit_doc(request: Request, id: str):
    r = requests.get(url="http://backend:8000/doc/" + id)
    j = r.json()
    m = j["doc"]
    return templates.TemplateResponse("edit.html", {"request": request, "markdown": m})


@app.post("/doc")
async def create_doc(md: schemas.MarkDown):
    body = {"doc": md.doc}
    resp = requests.post(url="http://backend:8000/doc/", json=body)
    js = resp.json()
    return {"doc": str(js["doc"]), "editId": str(js["editId"])}
