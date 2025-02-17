from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50
    with pytest.raises(ZeroDivisionError):
        _ = convert('1/0')
    with pytest.raises(ValueError):
        _ = convert('2/1')

def test_gauge():
    assert gauge(29) == '29%'
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
