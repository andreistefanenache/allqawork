import pytest
from programs import factorial
def test_factorial():
    assert factorial.fact(10) == 3628800
    assert factorial.fact(11) > factorial.fact(10)
    assert factorial.fact(1) == 1
