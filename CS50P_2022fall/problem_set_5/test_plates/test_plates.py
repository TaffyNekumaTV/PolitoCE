from plates import is_valid

def test_more_than_6():
    assert is_valid('ab12345') == False
    assert is_valid('afafafaf') == False

def test_less_than_2():
    assert is_valid('a') == False
    assert is_valid('1') == False

def test_isalpha():
    assert is_valid('1faf') == False
    assert is_valid('faff') == True
    assert is_valid('12ffff') == False
    assert is_valid('123') == False

def test_isnumeric():
    assert is_valid('faf11f') == False
    assert is_valid('fa111') == True

def test_zero():
    assert is_valid('af013') == False
    assert is_valid('aa120') == True

def test_an():
    assert is_valid('ff...') == False
    assert is_valid('G   ') == False
