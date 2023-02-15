import numpy as np
import pytest

from unpackqa.tools.unpackbits import unpackbits, int16_to_bits, packbits


def test_compare_unpack_methods():
    """
    Core unpacking function should have the exact results as a slower 
    string based method
    """
    arr = np.arange(2046)
    
    method1 = np.array([int16_to_bits(int(x)) for x in arr], dtype=np.uint8)
    method2 = unpackbits(arr, num_bits=16)
    
    # bit axis at the end to match method1
    method2 = np.moveaxis(method2, source = 0, destination = -1)

    assert (method1 == method2).all()

@pytest.mark.parametrize('num_bits', [8,16,32])
def test_unpackbits_shape_retention(num_bits):
    """
    Core unpacking function should take an arbitrary shape and return the
    same with 1 new axis of length num_bits at axis position 0.
    """
    high_range = (2**num_bits)-1
    arr1 = np.random.randint(low=0, high=high_range, size=64)
    arr2 = np.random.randint(low=0, high=high_range, size=64**2).reshape((64,64))
    arr3 = np.random.randint(low=0, high=high_range, size=64**3).reshape((64,64,64))
    arr4 = np.random.randint(low=0, high=high_range, size=64*21*42).reshape((64,21,42))
    
    test_result = [
        unpackbits(arr1, num_bits=num_bits).shape == (num_bits,64),
        unpackbits(arr2, num_bits=num_bits).shape == (num_bits,64,64),
        unpackbits(arr3, num_bits=num_bits).shape == (num_bits,64,64,64),
        unpackbits(arr4, num_bits=num_bits).shape == (num_bits,64,21,42),
        ]
    
    assert all(test_result)

@pytest.mark.parametrize('num_bits', [8,16,32])
def test_unpack_to_pack(num_bits):
    """packbits should reverse unpackbits"""
    high_range = (2**num_bits)-1
    arr1 = np.random.randint(low=0, high=high_range, size=64)
    arr2 = np.random.randint(low=0, high=high_range, size=64**2).reshape((64,64))
    arr3 = np.random.randint(low=0, high=high_range, size=64**3).reshape((64,64,64))
    arr4 = np.random.randint(low=0, high=high_range, size=64*21*42).reshape((64,21,42))
    
    test_results = [
        (arr1 == packbits(unpackbits(arr1, num_bits=num_bits), num_bits=num_bits)).all(),
        (arr2 == packbits(unpackbits(arr2, num_bits=num_bits), num_bits=num_bits)).all(),
        (arr3 == packbits(unpackbits(arr3, num_bits=num_bits), num_bits=num_bits)).all(),
        (arr4 == packbits(unpackbits(arr4, num_bits=num_bits), num_bits=num_bits)).all(),
        ]
    
    assert all(test_results)