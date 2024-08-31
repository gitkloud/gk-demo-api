import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello"}

@app.get("/v1/oauth")
def auth():
    return {"Authentication Completed"}

@app.post("/v1/users")
def auth():
    return {"users created Completed"}

@app.get("/v1/users/{user_name}")
def auth(user_name):
    return {"users list are" : user_name}

@app.put("/v1/users")
def auth():
    return {"users info replaced Completed"}

@app.delete("/v1/users")
def auth():
    return {"user deleted Completed"}

@app.get("/v2/oauth")
def auth():
    return {"Authentication Completed"}

@app.get("/items/{item_id}")
def list_items(item_id):
    return {"list items": item_id}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug")
