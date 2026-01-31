import pytest
from mymodule import add, multiply

class TestAdd:
    def test_add_integers(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0
        assert add(-1.5, 1.5) == 0.0

    def test_add_strings(self):
        assert add("hello", "world") == "helloworld"
        assert add("", "test") == "test"

class TestMultiply:
    def test_multiply_integers(self):
        assert multiply(2, 3) == 6
        assert multiply(-2, 3) == -6
        assert multiply(0, 5) == 0

    def test_multiply_floats(self):
        assert multiply(1.5, 2.0) == 3.0
        assert multiply(-1.5, 2.0) == -3.0

    def test_multiply_zero(self):
        assert multiply(0, 100) == 0
        assert multiply(100, 0) == 0