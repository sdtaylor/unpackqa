import numpy as np

"""
Core of the package is here, implemented with some bitwise operations.
"""

def unpackbits(qa_array, num_bits):
    """
    Iterate thru each bit to see if its set or not. 
    
    This uses two bitwise operators. The left shift operator (<<), which is 
    native to python, and the bitwise_and function in numpy.
    
    This line shifts bits to the left
        bit_loc = 1 << bit
    It makes bit_loc the respective integer when that bit, and only that bit, is set.
    
    For example with 16 bits the integer 1 in binary is:
        '0000000000000001'
    shifting it 10 bits to the left to represent the bit 10 location produces:
        '0000010000000000'
    Which is the integer 1024    
    
    The bitwise_and statement of the qa_array and bit_loc will produce an 
    array with values 0 or 1024 indicating all the locations where that bit was set.
    This output is boolean but is converted to 0/1 when its put into the
    bit_array since bit_array as the dtype set to uint8.
    
    Note the returned shape here has the bit axis in position 0 for easier 
    indexing. In the user facing unpack_to_array function the final *mask* 
    values are in the last axis (position -1).
    
    Parameters
    ----------
    qa_array : np.array
        An int-line numpy array.
    num_bits : int
        Number of bits to expand to.
        
    Returns
    -------
    np.array int8
        0/1 array with size (num_bits,) + qa_array.shape
        
    """
    original_shape = qa_array.shape
    new_shape = (num_bits,) + original_shape
    
    bit_array = np.empty(shape = new_shape, dtype=np.uint8)
    
    for bit in range(num_bits):
        bit_loc = 1<<bit
        bit_array[bit] = np.bitwise_and(qa_array,bit_loc) == bit_loc
    
    return bit_array


"""
This bit unpacking uses string formating to do the job. Not as fast as the
numpy method in unpackbits.py, but is easier to understand and is used for sanity
check testing. 
"""

def int16_to_bits(x):
    """
    Unpack a 16 bit integer into binary fields. See the syntax for
    this here https://docs.python.org/3/library/string.html#format-specification-mini-language
    
    Parameters
    ----------
    x : int16
        single integer.

    Returns
    -------
    List of binary fields aligned so int16_to_bits(1024)[0] = bit 0

    """
    assert isinstance(x, int), 'x should be integer'
    return [int(b) for b in f'{x:016b}'.format(x)[::-1]]