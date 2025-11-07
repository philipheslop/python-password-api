from urllib.request import urlopen, Request
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os
import json

load_dotenv() # Loading environment variables from .env

app = FastAPI()
header_scheme = APIKeyHeader(name="x-key")
request = Request(url=os.getenv("DATA_URL"), headers={"User-Agent": "Mozilla/5.0"})
response = urlopen(request)
data = json.loads(response.read())
#print(data)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def rate_password(password: str) -> str:
    length = len(password)
    if length < 6:
        return "Weak"
    elif 6 <= length < 10:
        return "Moderate"
    else:
        return "Strong"


@app.post("/rate-password/")
def rate_password_endpoint(password: str, key: str = Depends(header_scheme)):
    if key == os.getenv("API_KEY"):
        return {"password": password, "strength": rate_password(password)}
    return {"error": "Unauthorized"}, 401

@app.get("/key/")
async def read_items(key: str = Depends(header_scheme)):
    return {"key": key}