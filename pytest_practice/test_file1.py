import pytest

def fun(x):
    x + 1
    

def test_answer():
    assert fun(3) == 5

