from fastapi import FastAPI

app = FastAPI(title="Blog Api")

@app.get("/")
def read_root():
    return{"message":"welcome to the blog api"}