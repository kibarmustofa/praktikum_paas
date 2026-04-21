from app import calculate

def test_add():
    assert calculate(2, 3, "+") == 5

def test_sub():
    assert calculate(5, 2, "-") == 3

def test_mul():
    assert calculate(2, 3, "*") == 6

def test_div():
    assert calculate(6, 2, "/") == 3