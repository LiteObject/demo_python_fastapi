from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

def get(url: str):    
    response = requests.get(url)
    print(response.text)