import pytest 

@pytest.mark.parametrize("data,expected", [((3, 5), 8), ((2, 4), 6), ((6, 9), 15)])
def test_add(data, expected):
    assert add(*data) == expected

def add(a, b):
    """A ne pas mettre ici, c'est juste pour l'exemple..."""
    return a + b