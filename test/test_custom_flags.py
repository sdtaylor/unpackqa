import pytest
import numpy as np

from unpackqa import (unpack_to_array,
                        unpack_to_dict, 
                        list_products,
                        list_qa_flags
                        )

from unpackqa import InvalidProductSpec


"""
Custom flag specifications are allowed. Here test that capability with some
simple flag specs, and test the internal spec validations with some
invalid flag specs. 
"""

qa_array = np.array([[8,8,8],
                     [16,16,16],
                     [255,255,255]])



valid_test_cases = [
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[14]},
     'max_value' : 65535,
     'num_bits'  : 16},   

    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[3]},
     'max_value' : 255,
     'num_bits'  : 8},  

    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[4,5]},
     'max_value' : 255,
     'num_bits'  : 8},    
    
    ]


invalid_test_cases = [
    # bits out of order
    {'flag_info':{'flag1_description':[1],
                  'flag2_description':[0],
                  'flag3_description':[14]},
     'max_value' : 65535,
     'num_bits'  : 16},   

    # bits too large for num_bits
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[16]},
     'max_value' : 255,
     'num_bits'  : 8},  

    # empty flag entry
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[],
                  'flag3_description':[4,5]},
     'max_value' : 255,
     'num_bits'  : 8},    
    
    # negative bit entry
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[-1],
                  'flag3_description':[4,5]},
     'max_value' : 255,
     'num_bits'  : 8},    

    # max size does not match num_bits
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[4,5]},
     'max_value' : 500,
     'num_bits'  : 8},

    # missing num_bits
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[4,5]},
     'max_value' : 500},

    # missing max_value
    {'flag_info':{'flag1_description':[0],
                  'flag2_description':[1],
                  'flag3_description':[4,5]},
     'num_bits'  : 8},
    ]


@pytest.mark.parametrize('custom_spec', valid_test_cases)
def test_valid_spec_to_array(custom_spec):
    """Custom specs result in correctly shaped array"""
    output = unpack_to_array(qa_array, product = custom_spec)
    n_flags = len(custom_spec['flag_info'])
    assert output.shape == qa_array.shape + (n_flags,)

@pytest.mark.parametrize('custom_spec', valid_test_cases)
def test_valid_spec_to_dict(custom_spec):
    """Custom specs result in correct dictionary"""
    output = unpack_to_dict(qa_array, product = custom_spec)
    flag_names = custom_spec['flag_info'].keys()
    
    flags_present = [f in output for f in flag_names]
    assert all(flags_present)

@pytest.mark.parametrize('custom_spec', invalid_test_cases)
def test_invalid_spec_to_array(custom_spec):
    """Invalid specs should throw an error"""
    with pytest.raises(InvalidProductSpec):
        output = unpack_to_dict(qa_array, product = custom_spec)

@pytest.mark.parametrize('custom_spec', invalid_test_cases)
def test_invalid_spec_to_dict(custom_spec):
    """Invalid specs should throw an error"""
    with pytest.raises(InvalidProductSpec):
        output = unpack_to_dict(qa_array, product = custom_spec)
