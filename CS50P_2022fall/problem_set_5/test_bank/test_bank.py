from bank import value

def test_h():
    assert value('H1') == 20
    assert value('h1') == 20

def test_hello():
    assert value('HEllo') == 0
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_g():
    assert value('ff') == 100
    assert value('...') == 100
    assert value('ggghello') == 100
