import pytest
from programs import list_of_squares
def test_list_of_squares():
    assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}
