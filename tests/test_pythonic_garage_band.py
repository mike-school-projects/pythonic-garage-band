import pytest
from pythonic_garage_band.pythonic_garage_band import Band

def test_band_name():
    actual = Band().name
    expectation = 'test'
    assert actual == expectation