from fastapi import FastAPI
from pydantic import BaseModel
#调用fastAPI接口
app=FastAPI()

users = [
    {"id": 1, "name": "Alice", "age": 23},
    {"id": 2, "name": "Bob", "age": 25}
]


class User(BaseModel):
    name:str
    age:int
    
@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user['id']==user_id:
            return user
    return {"error":"user not found"}

@app.post("/users")
def create_user(user: User):
    new_user={
        "id":len(users)+1,
        "name":user.name,
        "age":user.age
    }
    users.append(new_user)
    
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for user in users:
        if user["id"]==user_id:
            users.remove(user)
            return {"message":"deleted"}
    return {"error":"user not found"}