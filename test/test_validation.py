import pytest
import numpy as np

from pyUnpackQA.Landsat import L8C2L2_QAPixel

l8 = L8C2L2_QAPixel()

def test_max_value():
    """Raise error when values is too large"""
    too_large_qa = np.array([1e6, 2e6], dtype=np.int64)
    with pytest.raises(ValueError):
        l8.unpack_to_dict(too_large_qa)

def test_neg_values():
    """bit arrays should not have negative numbers"""
    neg_qa = np.array([-2,-3], dtype=np.int64)
    with pytest.raises(ValueError):
        l8.unpack_to_dict(neg_qa)
    
def test_array_type():
    """only integer arrays should be passed"""
    qa = np.array([1024,2048], dtype=np.float64)
    with pytest.raises(TypeError):
        l8.unpack_to_dict(qa)

def test_array():
    """Only numpy arrays"""
    qa = [128,128]
    with pytest.raises(TypeError):
        l8.unpack_to_dict(qa)

def test_invalid_flag():
    qa = np.array([64,128], dtype=np.int16)
    with pytest.raises(ValueError):
        l8.unpack_to_dict(qa, flags=['asdf'])
