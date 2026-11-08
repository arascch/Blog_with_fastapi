from fastapi import FastAPI , HTTPException

app = FastAPI(title="Blog Api")


posts = [
    {"id": 1, "title":"hello World" , "content":"my first post"},
    {"id": 2, "title":"learning Fastapi" , "content":"tyoe hints do a lot of works"},
    {"id": 3, "title":"why my sql still matters" , "content":"Databases outlive frameworks"},
]


@app.get("/")
def read_root():
    return{"message":"welcome to the blog api"}


@app.get("/posts")
def list_posts(skip:int = 0 , limit:int=10):
    return posts[skip:skip+limit]

@app.get("/posts/{post_id}")
def get_post(post_id:int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404 , detail="post not found")