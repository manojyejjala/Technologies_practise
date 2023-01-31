import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    @pytest.mark.keyword
    def test_two(self):
        x = "hello"
        assert hasarrt(x, "check")

