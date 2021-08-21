
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