from numpy import issubdtype, arange, dtype, floating

"""
This bit of code is by StackOverflow user "Ross" as of December 1, 2020.
Used here under the CC BY-SA 4.0 license https://creativecommons.org/licenses/by-sa/4.0/

https://stackoverflow.com/a/51509307/6615512

It will unpack an arbitrarily shaped numpy array into an arbitrary number of bits.


Assuming 16 bits array shapes become
(8,) -> (8,16)
(128,128) -> (128,128,16) 
"""

def unpackbits(x, num_bits):
    if issubdtype(x.dtype, floating):
        raise ValueError("numpy data type needs to be int-like")
    xshape = list(x.shape)
    x = x.reshape([-1, 1])
    mask = 2**arange(num_bits, dtype=x.dtype).reshape([1, num_bits])
    return (x & mask).astype(bool).astype(int).reshape(xshape + [num_bits])