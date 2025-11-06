from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

def rate_password(password: str) -> str:
    length = len(password)
    if length < 6:
        return "Weak"
    elif 6 <= length < 10:
        return "Moderate"
    else:
        return "Strong"


@app.post("/rate-password/")
def rate_password_endpoint(password: str):
    return {"password": password, "strength": rate_password(password)}