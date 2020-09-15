import pytest

def inc(x):
    return x + 1

class TestClass:
    def test_inc(self):
        x = 1
        assert inc(x) == 2

    def test_inc2(self):
        x = 2
        assert inc(x) == 2