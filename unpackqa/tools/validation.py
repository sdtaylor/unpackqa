

class InvalidProductSpec(ValueError):
    """
    Error class for when an invalid custom specification is passed to the `product` argument.
    """

# Tests to validate custom product flag specifications. These specs can be declared
# via a dictionary in the unpack_to_* functions.
# These tests are also used validate the internally configured products during self testing.

def product_info_is_dict(product_info):
    if not isinstance(product_info, dict):
            raise TypeError('product info should be a dictonary')

def product_info_has_required_entries(product_info):
    required_entries = ['flag_info','num_bits','max_value']
    if not all([e in product_info for e in required_entries]):
        raise InvalidProductSpec('product info missing required entires')

def flag_info_is_non_empty_dict(product_info):
    flag_info = product_info['flag_info']
    if not isinstance(flag_info, dict) and len(flag_info) > 0:
        raise InvalidProductSpec('flag_info entry should be non-empty dictionary')

def flag_info_bit_list_non_empty(product_info):
    """Bit entries for each flag a non-empty lists"""
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        flags_valid.append(isinstance(bits, list) and len(bits) > 0)
    if not all(flags_valid):
        raise InvalidProductSpec('bit entries for each flag should be non-empty lists')
        
def flag_info_bits_non_neg_ints(product_info):
    """Bits within each list should be non-negative integers"""
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        bits_non_neg = all([b >=0 for b in bits])
        bits_values_are_ints = all([isinstance(b,int) for b in bits])
        flags_valid.append(bits_non_neg and bits_values_are_ints)
    if not all(flags_valid):
        raise InvalidProductSpec('bits should be non-negative integers')
        
def flag_info_flag_is_str(product_info):
    """The key values within 'flag_info' should be strings"""
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        flags_valid.append(isinstance(flag_name,str))
    if not all(flags_valid):
        raise InvalidProductSpec('flag descriptions should be strings')
        
def bits_are_only_used_once(product_info):
    """Bits should not be listed twice"""
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    if not len(set(all_listed_bits)) == len(all_listed_bits):
        raise InvalidProductSpec('duplicate bits detected')

def bits_are_reasonable(product_info):
    """Very unlikely to encounter anything beyond 32 bit integers for masks"""
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    if not all([b <= 32 for b in all_listed_bits]):
        raise InvalidProductSpec('Bits greater than 32 listed')

def bits_do_not_exceed_bit_size(product_info):
    """The largest bit should be <= the number of bits"""
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    if not max(all_listed_bits) < product_info['num_bits']:
        raise InvalidProductSpec('Largest bit flag is greater than num_bits')
        
def max_value_matches_num_bits(product_info):
    """ Maximum value listed should be < the largest size given num_bits"""
    if product_info['max_value'] >= 2**product_info['num_bits']:
        raise InvalidProductSpec('max_value is >= 2**num_bits')
        
def bits_are_ordered(product_info):
    """Bits should be listed smallest to largest"""
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    if not all_listed_bits == sorted(all_listed_bits):
        raise InvalidProductSpec('bits are not listed smallest to largest')

def validate_product_spec(product_info):
    """Used in user facing functions to check custom speciifcaitons"""
    product_info_is_dict(product_info)
    product_info_has_required_entries(product_info)
    flag_info_is_non_empty_dict(product_info)
    flag_info_bit_list_non_empty(product_info)
    flag_info_bits_non_neg_ints(product_info)
    flag_info_flag_is_str(product_info)
    bits_are_only_used_once(product_info)
    bits_are_reasonable(product_info)
    bits_do_not_exceed_bit_size(product_info)
    max_value_matches_num_bits(product_info)
    bits_are_ordered(product_info)
