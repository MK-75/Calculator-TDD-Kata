# Test cases for the calculator code

import pytest
from calculator import add

# Test for addition of two numbers
def test_add():
    result = add(" ")
    assert result == 0

    result = add("1")
    assert result == 1

    result = add("1,2")
    assert result == 3

    result = add("6,5")
    assert result == 11
