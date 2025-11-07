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
    - 

Extras:
-------

6. Make a client website
    - use React

7. Make a test
