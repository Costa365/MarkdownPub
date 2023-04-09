from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/doc/{id}", response_class=HTMLResponse)
async def root(request: Request, id:str):
    r = requests.get(url='http://backend:8000/doc/'+id)
    j = r.json()
    m = j['doc']
    return templates.TemplateResponse("doc.html", {"request": request, "markdown":m})
