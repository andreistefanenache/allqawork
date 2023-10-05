import counter

def test_count_integers():
    assert counter.count([1,2,3,3,4],3) == 2
def test_count_string():
    assert counter.count("this is my string","i") == 3
