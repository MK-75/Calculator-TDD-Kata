# Test cases for the calculator code

import pytest
from calculator import add

# Test for addition of two numbers
def test_add():
    result = add(" ")
    assert result == 0
