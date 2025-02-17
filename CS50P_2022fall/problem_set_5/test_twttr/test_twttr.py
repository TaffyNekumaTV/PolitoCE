from twttr import shorten

# print(shorten('aaabbb'))
def test_upper():
    assert shorten('AAAB') == 'B'
    assert shorten('ObO') == 'b'

def test_lower():
    assert shorten('aaaB') == 'B'
    assert shorten('ooB') == 'B'

def test_number():
    assert shorten('3') == '3'

def test_punctuation():
    assert shorten('.') == '.'
