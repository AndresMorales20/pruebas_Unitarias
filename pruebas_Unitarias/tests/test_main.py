import pytest
from app.main import validate_password

@pytest.mark.parametrize("password, expected", [
    ("StrongPassword123!", True),
    ("short123!", False),
    ("NOLOWER123!", False),
    ("NoUpper123!", False),
    ("NoNums!!!", False),
    ("NoSpaces123!", True),
])
def test_validate_password(password, expected):
    assert validate_password(password) == expected