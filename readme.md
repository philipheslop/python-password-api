Instructions
------------


* To Run server:
        (fastapi dev main.py)
        runs on: (127.0.0.1:8000)
* routes:
        /docs = fastApi docs/api test
        /rate-password = rout to POST password text to
* response shape:
        {
          "password": "password",
          "score": 7.5,
          "response": "Weak"
        }
         



Assumptions/Initial Thoughts:
-----------------------------

* This is an API service and not a full login/security system
* This means no _requirement_ to store a users table or similar (either as a DB or mocked data) - though this may be added as an extra
* The estimated time scale is approx 2 hours - it's important to stick to this to give an accurate impression of work done and to be fair to other candidates
* The approach I will take is to implement an MVP then use remaining time to improve

Implementation:
---------------

1. Python environment/FastAPI (using docs from https://fastapi.tiangolo.com)
    - install python3 & pip
    - make virtual environment
        (apt install python3.12-venv)
        (python -m venv .venv)
        (source .venv/bin/activate) --note: needs to be set per session
    - install fastAPI
        (pip install "fastapi[standard]")
    - setup git on github

2. 'hello world' fastAPI program.
    - setup routes e.g. '/' and '/rate_password'

3. Naive rate password
    - setup route
    - implement simple check

4. Adding Security
    - add API key
        (considered using synchronous or asyncronous encrtyption - decided that for MVP this is not needed but might be an extra)
    - use .env
        (note: have included .env in repository for assessment, this would be in .gitignore in production)

5. Improving password rating algorithm
    - identify payload url for top 200 passwords list
        (https://nordpass.com/next/worst-passwords-list/2024/b2c/all.json)
    - I have attempted to compose a novel scoring system for passwords:
    - Create a score based on the character distribution ('spread') of password (i.e. more variety is better)
    - Create a score based on the character category (upper,lower,num and special) uniformity (i.e. have similar amounts of each - opposite of spread)
    - I have used a basic statistical tool - Coefficient of Variation - to calulate these distribution based scores. This equation gives a measure of 'spread' of data. I have used the numpy library for this.

----------------------------------------------
2 hour mark - steps 1 - 5 took approx. 2 hours
----------------------------------------------

Extras:
-------

6. Make a client website (~45 mins - based on existing code/not built from scratch)
    - use React
    - add CORS to api (to test on same machine)
 
7. Make a test (~30 mins)
    - install pytest
        (pip install pytest)
