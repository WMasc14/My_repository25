from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import os

app = FastAPI()

if os.path.isdir("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
else:
    print("Warning: static directory not found, skipping static mount")

templates = Jinja2Templates(directory="templates")

DATAFRAME = None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "resultados": []})

@app.post("/upload")
async def upload_planilha(request: Request, file: UploadFile = File(...)):
    global DATAFRAME
    ext = file.filename.split(".")[-1]

    if ext == "csv":
        DATAFRAME = pd.read_csv(file.file)
    else:
        DATAFRAME = pd.read_excel(file.file)

    return RedirectResponse("/", status_code=303)

@app.post("/buscar", response_class=HTMLResponse)
async def buscar(request: Request):
    global DATAFRAME
    form = await request.form()
    termo = form.get("busca", "").lower()
    resultados = []

    if DATAFRAME is not None:
        for _, row in DATAFRAME.iterrows():
            texto = " ".join(str(v).lower() for v in row.values)
            if termo in texto:
                resultados.append(row.to_dict())

    return templates.TemplateResponse("index.html", {
        "request": request,
        "resultados": resultados
    })