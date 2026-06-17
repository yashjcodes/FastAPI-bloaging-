from fastapi import FastAPI, Request
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



posts :list[dict] = [
       {
        "id": 1,
        "author": "John Doe",
        "title": "Introduction to FastAPI",
        "content": "FastAPI is a modern Python web framework for building APIs quickly and efficiently.",
        "date_posted": "2026-06-10"
    },
    {
        "id": 2,
        "author": "Alice Smith",
        "title": "Understanding Dependency Injection",
        "content": "Dependency Injection helps manage reusable components and keeps code clean.",
        "date_posted": "2026-06-11"
    },
]


app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/",include_in_schema=False ) #it will hide it from documantation
def home(request : Request):
    return templates.TemplateResponse(request, "home.html" , {"posts":posts})

@app.get("/ni")
def holi():
    return {"message":"holi h"}


@app.get("/api/post")
def get_posts():
    return posts