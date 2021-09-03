import pytest
import numpy as np

from unpackqa import unpack_to_array, unpack_to_dict

default_product = 'LANDSAT_8_C2_L2_QAPixel'

def test_max_value():
    """Raise error when values is too large"""
    too_large_qa = np.array([1e6, 2e6], dtype=np.int64)
    with pytest.raises(ValueError):
        unpack_to_dict(too_large_qa, product = default_product)

def test_neg_values():
    """bit arrays should not have negative numbers"""
    neg_qa = np.array([-2,-3], dtype=np.int64)
    with pytest.raises(ValueError):
        unpack_to_dict(neg_qa, product = default_product)
    
def test_array_type():
    """only integer arrays should be passed"""
    qa = np.array([1024,2048], dtype=np.float64)
    with pytest.raises(TypeError):
        unpack_to_dict(qa, product = default_product)

def test_array():
    """Only numpy arrays"""
    qa = [128,128]
    with pytest.raises(TypeError):
        unpack_to_dict(qa)

def test_single_value_int():
    """A singel value is fine as long as it's an int"""
    result = unpack_to_array(1, product = default_product)
    assert result is not None
    
def test_single_value_float():
    """No floats please"""
    with pytest.raises(TypeError):
        unpack_to_array(1.1, product = default_product)

def test_invalid_flag1():
    """Invalid flag names should raise an error"""
    qa = np.array([64,128], dtype=np.int16)
    with pytest.raises(ValueError):
        unpack_to_dict(qa, product = default_product, flags=['asdf'])

def test_invalid_flag2():
    """Non-list flag string should raise an error"""
    qa = np.array([64,128], dtype=np.int16)
    with pytest.raises(ValueError):
        unpack_to_dict(qa, product = default_product, flags='asdf')
    
def test_empty_flag_list():
    """Empty flag list should raise an error"""
    qa = np.array([64,128], dtype=np.int16)
    with pytest.raises(ValueError):
        unpack_to_dict(qa, product = default_product, flags=[])
