from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="templates/html")

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def registration(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")

from pydantic import BaseModel

class Cat(BaseModel):
    cat: str


@app.post("/data")
async def check(cat: Cat):
    print(cat.model_dump())
    return {"answer": 'success'}