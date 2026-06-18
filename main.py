from fastapi import FastAPI, Request
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException, status



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


@app.get("/",include_in_schema=False, name = "home" ) #it will hide it from documantation
@app.get("/post",include_in_schema=False, name = "post")
def home(request : Request):
    return templates.TemplateResponse(request, "home.html" , {"posts":posts})

@app.get("/ni")
def holi():
    return {"message":"holi h"}


@app.get("/api/post")
def get_posts():
    return posts


@app.get("/api/post/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")


   