from http.client import HTTPException
from typing import Optional, List
from uuid import uuid4, UUID

# from Tools.scripts.serve import app
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role

# instance of FASTAPI
app = FastAPI()

db: List[User] = [
    User(
        id = UUID("7cc20ebe-d24c-4495-b423-de8b5068fdcd"),
        first_name = "Priya",
        last_name = "Nayak",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id = UUID("57873b78-696a-483d-9174-78ee2f55d6e4"),
        # id = uuid4(), # id will change everytime we restart the application if we call the uuid4() function
        first_name = "Avinash",
        last_name = "Bawane",
        gender = Gender.male,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")

# to make asynchronous computation, we use async keyword
async def read_root():
    # if you use await, then you need to use async
    # await foo()
    return {"Hello": "Sir"}  # this is a JSON object of type key value

@app.get("/api/v1/users")
async def fetch_users():
    return db

#from our web browser we can only send GET request. We cannot send POST request.
#
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException (
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user}")
async def modify_user(user: User):
    for u in db:
        if u.id == user.id:
            




#starter code
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}