# Test cases for the calculator code

import pytest
from calculator import add

# Test for addition of two numbers
def test_add_two_numbers():
    result = add(" ")
    assert result == 0

    result = add("1")
    assert result == 1

    result = add("1,2")
    assert result == 3

    result = add("6,5")
    assert result == 11

    result = add("11000, 99999")
    assert result == 110999

# Test for the addition of n numbers
def test_add_numbers():
    result = add("1,2,3")
    assert result == 6

    result = add("5,6,7,8")
    assert result == 26

    result = add("10, 20, 30, 100")
    assert result == 160

    result = add("1,2,3,4,5")
    assert result == 15

    result = add("15, 20, 25, 30, 35")
    assert result == 125

# Test for errors than can occur while addition
def test_add_errors():
    error_msg = add("1,")
    assert error_msg == "Input is not correct"

    error_msg = add(",12,0")
    assert error_msg == "Input is not correct"

    error_msg = add("1|2|3")
    assert error_msg == "Input is not correct"
