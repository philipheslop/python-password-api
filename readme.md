Assumptions:
------------

This is an API service and not a full login/security system
This means no requirement to store a users table or similar (either as a DB or mocked data)

Implementation:
---------------

1. Python environment/FastAPI (using docs from https://fastapi.tiangolo.com)
    - install poetry
    - install pip
    - make virtual environment
        (apt install python3.12-venv)
        (python -m venv .venv)
        (source .venv/bin/activate) --note: needs to be set per session
    - install fastAPI
        (pip install "fastapi[standard]")

2. 'hello world' fastAPI program.
    - setup routes e.g. '/'

3. Naive rate password
    - setup route
    - impliment simple check

4. Adding Security

5. Improving password rating algorithm
