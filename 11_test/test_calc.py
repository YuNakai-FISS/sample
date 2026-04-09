from calc import add
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, 5, 15),
])

def test_add_param(a, b, expected):
    assert add(a, b) == expected