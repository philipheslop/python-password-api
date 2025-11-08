from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_cv_score():
    assert main.cv_score([]) == 0
    assert main.cv_score([5, 5, 5, 5]) == 0
    assert main.cv_score([1, 2, 3, 4, 5]) > 0

def test_validate_password():
    valid_password = "Aa1!aaaa"
    is_valid, message, score = main.validate_password(valid_password)
    assert is_valid
    assert message == "Password is valid"
    assert score > 0

    short_password = "Aa1!"
    is_valid, message, score = main.validate_password(short_password)
    assert not is_valid
    assert message == "Password must be between 8 and 256 characters"

    no_special_char_password = "Aa1aaaaa"
    is_valid, message, score = main.validate_password(no_special_char_password)
    assert not is_valid
    assert message == "Password must contain at least one digit, one uppercase letter, one lowercase letter, and one special character"

    common_password = "Qwerty123!"
    is_valid, message, score = main.validate_password(common_password)
    assert not is_valid
    assert message == "Password is too common"