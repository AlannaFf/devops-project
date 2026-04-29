from app import soma, subtracao

def test_soma_1():
    assert soma(2, 3) == 5

def test_soma_2():
    assert soma(0, 0) == 0

def test_soma_3():
    assert soma(-1, 1) == 0

def test_subtracao_1():
    assert subtracao(5, 3) == 2

def test_subtracao_2():
    assert subtracao(10, 5) == 5
