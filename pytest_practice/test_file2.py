#content of test_sysexit.py
import pytest


def f():
    raise SysytemExit(1)


def test_mytest():
    with pytest.raise(SystemExit):
        f()

