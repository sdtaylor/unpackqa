import numpy as np
import pytest

from pyUnpackQA.tools.unpackbits import unpackbits, int16_to_bits


def test_compare_unpack_methods():
    arr = np.arange(2046)
    
    method1 = np.array([int16_to_bits(int(x)) for x in arr], dtype=np.uint8)
    method2 = unpackbits(arr, num_bits=16)

    assert (method1 == method2).all()

def test_unpackbits_shape_retention():
    arr = np.random.randint(low=0, high=2048, size=128*128).reshape((128,128))
    bits = unpackbits(arr, num_bits = 16)
    assert bits.shape == (128,128,16)