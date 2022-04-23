import pytest
import numpy as np

from unpackqa import (unpack_to_array,
                      unpack_to_dict, 
                      pack_from_array,
                      pack_from_dict,
                      )



custom_spec1 = {'flag_info':{
                    'flag1_description':[0],
                    'flag2_description':[1],
                    'flag3_description':[2],
                    'flag4_description':[3],
                    'flag5_description':[4],
                    'flag6_description':[5,6,7],
                    
                    },
                'max_value' : 255,
                'num_bits'  : 8}

custom_spec2 = {'flag_info':{
                    'flag1_description':[0],
                    'flag2_description':[1],
                    'flag3_description':[2],
                    'flag4_description':[3],
                    'flag5_description':[4,5],
                    'flag6_description':[6],
                    'flag7_description':[7,8,9],
                    'flag8_description':[10,11],
                    'flag10_description':[12],
                    'flag11_description':[13],
                    'flag12_description':[14],
                    'flag13_description':[15],
                    },
                'max_value' : 65535,
                'num_bits'  : 16}

product_test_cases = [custom_spec1, custom_spec2]

@pytest.mark.parametrize('product_spec', product_test_cases)
def test_array_packing(product_spec):
    high_range = (2**product_spec['num_bits'])-1
    qa_array = np.random.randint(low=0, high=high_range, size=32**3).reshape((32,32,32))

    flag_array = unpack_to_array(qa_array, product=product_spec, flags='all')
    packed_array = pack_from_array(flag_array, product=product_spec, flags='all')
    
    assert (qa_array == packed_array).all()

@pytest.mark.parametrize('product_spec', product_test_cases)
def test_dict_packing(product_spec):
    high_range = (2**product_spec['num_bits'])-1
    qa_array = np.random.randint(low=0, high=high_range, size=32**3).reshape((32,32,32))

    flag_array = unpack_to_dict(qa_array, product=product_spec, flags='all')
    packed_array = pack_from_dict(flag_array, product=product_spec, flags='all')
    
    assert (qa_array == packed_array).all()







