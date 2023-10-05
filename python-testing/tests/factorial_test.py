import pytest
from programs import factorial
def test_factorial():
    assert factorial.fact(10) == 3628800
