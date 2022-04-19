from typing import Optional

from fastapi import FastAPI

# instance of FASTAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Sir"}  # this is a JSON object of type key value


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}