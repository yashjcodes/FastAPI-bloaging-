from fastapi import FastAPI, Request, HTTPException, status
#from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# pyrefly: ignore [missing-import]
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


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
@app.get("/posts",include_in_schema=False, name = "post")
def home(request : Request):
    return templates.TemplateResponse(request, "home.html" , {"posts":posts})


@app.get("/posts/{post_id}", include_in_schema=False, name="post_detail")
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            title = post["title"][:50]
            return templates.TemplateResponse(request, "post.html", {"post": post, "title": title})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
        


@app.get("/api/post")
def get_posts():
    return posts


@app.get("/api/post/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")

    ## StarletteHTTPException Handler
@app.exception_handler(StarletteHTTPException)
def general_http_exception_handler(request: Request, exception: StarletteHTTPException):
    message = (
        exception.detail
        if exception.detail
        else "An error occurred. Please check your request and try again."
    )

    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exception.status_code,
            content={"detail": message},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": exception.status_code,
            "title": exception.status_code,
            "message": message,
        },
        status_code=exception.status_code,
    )


### RequestValidationError Handler
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exception: RequestValidationError):
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            content={"detail": exception.errors()},
        )
    return templates.TemplateResponse(
        request,
        "error.html",
        {
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "title": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid request. Please check your input and try again.",
        },
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
    )


   