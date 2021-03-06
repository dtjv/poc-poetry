import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.py_demo.increment import increment, increment_all, increment_by_step


def test_should_increment_by_1():
    assert increment(3) == 4


def test_should_increment_by_default_step():
    assert increment_by_step(3) == 4


# manually define all cases. probably gonna miss something!
@pytest.mark.parametrize(
    "num, result",
    [
        (-2, -1),
        (0, 1),
        (3, 4),
        (101234, 101235),
    ],
)
def test_increment(num, result):
    assert increment(num) == result


# hypothesis generates way more edge cases!
@given(st.integers())
def test_increment_should_add_one(num):
    assert increment(num) == num + 1


@given(st.lists(st.integers()))
def test_increment_all(nums):
    expected = [n + 1 for n in nums]
    assert increment_all(nums) == expected
