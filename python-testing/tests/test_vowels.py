import pytest
from programs import vowels
def test_vowels():
    assert vowels.vowels("racecar") == 3
