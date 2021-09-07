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
numpy method in unpackbits, but is easier to understand and is used for sanity
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


def packbits(bit_array, num_bits):
    """
    Pack bit arrays into numeric arrays. This reverses unpackbits.

    Parameters
    ----------
    bit_array : np.array
        A integer array where the 0 axis is the bit axis.
    num_bits : int
        Integer size to use, either 8, 16, or 32. This should be
        the smallest size to accomidate the number of flag bits used.
        eg. if you are using flags to bit 10, num_bits should be 16.

    Returns
    -------
    An integer array with dtype matching num_bits. Shape will match 
    bit_array minus the 0 axis, ie. bit_array.shape[1:]

    """
    #TODO: a lot of processing time is from these initial checks. They 
    # could be removed or done more efficiently if speed ups are needed. 
    if num_bits not in [8,16,32]:
        raise TypeError('num_bits should be 8, 16, or 32')
    if bit_array.shape[0] > num_bits:
        raise TypeError('bit_array not large enought for num_bits')
    
    if not np.issubdtype(bit_array.dtype, np.integer):
        raise TypeErorr('bit_array not an integer dtype')
    if bit_array.max() > 1:
        raise TypeError('values >1 in bit_array')
    if bit_array.min() < 0:
        raise TypeError('values <0 in bit_array')
    
    if num_bits == 8:
        dtype = np.uint8
    elif num_bits == 16:
        dtype = np.uint16
    elif num_bits == 32:
        dtype = np.uint32
    
    # need bit_array dtype as the correct number of bits to compare with
    bit_array = bit_array.astype(dtype)
    
    numeric_from_bits = np.zeros(bit_array.shape[1:], dtype=dtype)
    
    for bit in range(num_bits):
        bit_loc = bit_array[bit] << bit
        numeric_from_bits = np.bitwise_or(numeric_from_bits, bit_loc)
    
    return numeric_from_bits