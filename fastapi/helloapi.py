from fastapi import FastAPI

app = FastAPI()

@app.get("/getname/{name}")
async def root(name):
    return{"message": "Hello, "+name}