import pytest
import numpy as np

from pyUnpackQA import (unpack_to_array,
                        unpack_to_dict, 
                        list_products,
                        list_qa_flags
                        )

from pyUnpackQA.product_loader import all_products

"""
Validating product definitions.
"""

qa_array = np.array([[8,8,8],
                     [16,16,16],
                     [255,255,255]])

all_product_identifiers = list_products(sensor='all')

def test_product_ids_are_unique():
    """No duplicate product identifers"""
    assert len(all_product_identifiers) == len(set(all_product_identifiers))

@pytest.mark.parametrize('product', all_product_identifiers)
def test_qa_flag_list(product):
    """Lists of flags should be available for each product"""
    flags = list_qa_flags(product = product)
    assert len(flags) > 0


"""
Several tests for flag info format. 
Within product_info the 'flag_info' entry
should be a dictonary with key value pairs:
    'flag name':[bit0,bit1,..]    
Where flag name is a str, with a value of a list. List entries
are non-negative ints.
"""

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_info_is_dict(product):
    """Flag info entry should be dictonary"""
    product_info = all_products[product]
    assert isinstance(product_info['flag_info'], dict)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_info_bit_list_non_empty(product):
    """Bit entries for each flag a non-empty lists"""
    product_info = all_products[product]
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        flags_valid.append(isinstance(bits, list) and len(bits) > 0)
    assert all(flags_valid)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_info_bits_non_neg_ints(product):
    """Bits within each list should be non-negative integers"""
    product_info = all_products[product]
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        bits_non_neg = all([b >=0 for b in bits])
        bits_values_are_ints = all([isinstance(b,int) for b in bits])
        flags_valid.append(bits_non_neg and bits_values_are_ints)
    assert all(flags_valid)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_info_flag_is_str(product):
    """The key values within 'flag_info' should be strings"""
    product_info = all_products[product]
    flags_valid = []
    for flag_name, bits in product_info['flag_info'].items():
        flags_valid.append(isinstance(flag_name,str))
    assert all(flags_valid)

"""
Various tests for bit values
"""

@pytest.mark.parametrize('product', all_product_identifiers)
def test_bits_are_only_used_once(product):
    """Bits should not be listed twice"""
    product_info = all_products[product]
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    assert len(set(all_listed_bits)) == len(all_listed_bits)
    
@pytest.mark.parametrize('product', all_product_identifiers)
def test_bits_match_max_value(product):
    """The largest bit should be < the max integer value"""
    product_info = all_products[product]
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    assert 2**max(all_listed_bits) < product_info['max_value']

@pytest.mark.parametrize('product', all_product_identifiers)
def test_bits_are_ordered(product):
    """Bits should be listed smallest to largest"""
    product_info = all_products[product]
    all_listed_bits = []
    for flag_name, bits in product_info['flag_info'].items():
        all_listed_bits.extend(bits)
        
    assert all_listed_bits == sorted(all_listed_bits)