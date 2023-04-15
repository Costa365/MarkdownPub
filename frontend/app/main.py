import requests
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "backend": "http://127.0.0.1:8000"}
    )


@app.get("/doc/{id}", response_class=HTMLResponse)
async def get_doc(request: Request, id: str):
    r = requests.get(url="http://backend:8000/doc/" + id)
    if r.status_code == 200:
        j = r.json()
        m = j["doc"]
        return templates.TemplateResponse(
            "doc.html", {"request": request, "markdown": m}
        )
    else:
        raise HTTPException(status_code=404, detail=f"Document {id} not found")


@app.get("/edit/{id}/{eid}", response_class=HTMLResponse)
async def edit_doc(request: Request, id: str):
    r = requests.get(url="http://backend:8000/doc/" + id)
    if r.status_code == 200:
        j = r.json()
        m = j["doc"]
        return templates.TemplateResponse(
            "edit.html",
            {"request": request, "markdown": m, "backend": "http://127.0.0.1:8000"},
        )

    else:
        raise HTTPException(status_code=404, detail=f"Document {id} not found")
