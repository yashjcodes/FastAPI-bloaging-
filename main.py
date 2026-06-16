from fastapi import FastAPI
from fastapi.responses import HTMLResponse
post :list[dict] = [
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

@app.get("/", response_class=HTMLResponse ,include_in_schema=False)
@app.get("/post", response_class=HTMLResponse ,include_in_schema=False)

def home():
    return f"<h1>{post[0]['title']}</h1>"

@app.get("/ni")
def holi():
    return {"message":"holi h"}


@app.get("/api/post")
def get_posts():
    return post