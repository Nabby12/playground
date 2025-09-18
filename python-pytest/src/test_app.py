import app as utils
import pytest

test_cases = [
    {"input": [1, 2, 3], "want": 6},
    {"input": [], "want": 0},
    {"input": [-1, -2, -3], "want": -6},
    {"input": [-1, 2, -3, 4], "want": 2},
]


@pytest.mark.parametrize("case", test_cases)
def test_main(case):
    assert utils.main(case["input"]) == case["want"]
