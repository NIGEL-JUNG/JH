from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

# static 폴더 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates 폴더 연결
templates = Jinja2Templates(directory="templates")


@app.get("/users/{user_name}")
async def welcome():
    return templates.TemplateResponse()
