from urllib.request import urlopen, Request
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json
import numpy as np

load_dotenv() # Loading environment variables from .env

app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # add your deployed frontend origin(s) here
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # use ["*"] only for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],       # include custom headers like "x-key"
)
header_scheme = APIKeyHeader(name="x-key")
request = Request(url=os.getenv("DATA_URL"), headers={"User-Agent": "Mozilla/5.0"})
response = urlopen(request)
data = json.loads(response.read())
#print(data)
filtered_data = list(map(lambda item: item["Password"], data))
#print(filtered_data)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def cv_score(data: list[int]) -> int:
    if len(data) == 0:
        return 0
    
    range = max(data) - min(data)
    if range == 0:
        return 0

    # Coefficient of Variation measures how different the values are from each other
    # We normalize it to be between 0 and 1, then scale to 0-10
    sd = np.std(data)
    mean = np.mean(data)
    cv = np.clip(sd/mean, 0, 1) # coefficient of variation
    score = int(cv * 10)
    # print(f"Data: {data}, Range: {range}, SD: {sd}, CV: {cv}, Score: {score}")
    return score

def validate_password(password: str) -> {bool, str, int }:
    score = 0

    if not password:
        return False, "Password is required", score

    length = len(password)
    if length < 8 or length > 256:
        return False, "Password must be between 8 and 256 characters", score

    special_characters = "\"!@#$%^&*()-+?_=,<>/\""

    num_digits = num_upper = num_lower = num_special = 0

    for char in password:
        if char in special_characters:
            num_special += 1
        elif char.isdigit():
            num_digits += 1
        elif char.isupper():
            num_upper += 1
        elif char.islower():
            num_lower += 1
        else:
            return False, f"Invalid character detected: {char}", score

    if num_digits == 0 or num_upper == 0 or num_lower == 0 or num_special == 0:
        return False, "Password must contain at least one digit, one uppercase letter, one lowercase letter, and one special character", score

    if password in filtered_data:
        return False, "Password is too common", score

    # we want categories to be evenly distributed
    category_weight = 0.5
    category_cv_score = 10 - cv_score([num_digits, num_upper, num_lower, num_special])
    
    # we want characters to be as different from each other as possible
    password_weight = 2
    password_score = cv_score(list(password.encode('utf-8')))

    score += category_weight * category_cv_score + password_weight * password_score

    if length < 10:
        score += 0
    elif 10 <= length < 20:
        score += 2
    else:
        score += 3
    return True, "Password is valid", score

def rate_password(password: str) -> {str, int}:
    is_valid, error_message, score = validate_password(password)
    if not is_valid:
        return error_message, -1

    return "Strong" if score >= 12 else "Moderate" if score >= 8 else "Weak", score


@app.post("/rate-password/")
def rate_password_endpoint(password: str, key: str = Depends(header_scheme)):
    if key == os.getenv("API_KEY"):
        return {"password": password, "score": rate_password(password)[1], "response": rate_password(password)[0]}
    return {"error": "Unauthorized"}, 401

@app.get("/key/")
async def read_items(key: str = Depends(header_scheme)):
    return {"key": key}