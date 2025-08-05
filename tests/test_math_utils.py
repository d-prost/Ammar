import os
import sys
import pytest

# Ensure root directory is on sys.path for module import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math_utils


def test_factorial_zero():
    assert math_utils.factorial(0) == 1


def test_factorial_positive():
    assert math_utils.factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        math_utils.factorial(-1)
