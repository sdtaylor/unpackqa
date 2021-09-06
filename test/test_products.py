import pytest
import numpy as np

from unpackqa import (unpack_to_array,
                        unpack_to_dict, 
                        list_products,
                        list_qa_flags
                        )

from unpackqa.tools.validation import (product_info_has_required_entries,
                                       flag_info_is_non_empty_dict,
                                       flag_info_bit_list_non_empty,
                                       flag_info_bits_non_neg_ints,
                                       flag_info_flag_is_str,
                                       bits_are_only_used_once,
                                       bits_are_reasonable,
                                       bits_do_not_exceed_bit_size,
                                       max_value_matches_num_bits,
                                       bits_are_ordered,
                                       )

from unpackqa.tools.validation import InvalidProductSpec

from unpackqa.product_loader import all_products

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
    
@pytest.mark.parametrize('product', all_product_identifiers)
def test_product_info_is_dict(product):
    """product_info entry should be dictonary"""
    product_info = all_products[product]
    assert isinstance(product_info, dict)


"""
Several tests for all products configred within the package.
Within product_info the 'flag_info' entry
should be a dictonary with key value pairs:
    'flag name':[bit0,bit1,..]    
Where flag name is a str, with a value of a list. List entries
are non-negative ints.

These same tests are used to validate user passed custom specifications, so
instead of essentially writing a new test function for each, just iterate 
over them and create some informative output if 1 or more fails.
"""

test_list = [('product info does not have required entries',product_info_has_required_entries),
             ('flag_info is not dictionary, or is empty', flag_info_is_non_empty_dict),
             ('flag_info has empty lists',flag_info_bit_list_non_empty),
             ('flag_info has negative and/or non-int values',flag_info_bits_non_neg_ints),
             ('flag_info keys are not strings',flag_info_flag_is_str),
             ('duplicate bits detected',bits_are_only_used_once),
             ('bits are larger than needed for even a 32 bit int', bits_are_reasonable),
             ('largest bit is greater than num_bits',bits_do_not_exceed_bit_size),
             ('max_value is >=  2**num_bits',max_value_matches_num_bits),
             ('bits are out of order',bits_are_ordered),
             ]

@pytest.mark.parametrize('product', all_product_identifiers)
def test_product_info(product):
    product_info = all_products[product]
    failed_tests = []
    tests_failed = False
    for test_message, test_function in test_list:
        try:
            test_function(product_info)
        except InvalidProductSpec:
            tests_failed = True
            failed_tests.append(test_message)
    
    if tests_failed:
        error_message = '{} failed tests for {}\n'.format(len(failed_tests), product)
        error_message = error_message + '\n'.join(['{}. {}'.format(i+1,m) for i,m in enumerate(failed_tests)])
        assert False, error_message

