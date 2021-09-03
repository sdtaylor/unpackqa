import pytest
import numpy as np

from unpackqa import (unpack_to_array,
                        unpack_to_dict, 
                        list_products,
                        list_qa_flags
                        )

# Given a list of actual QA values, ensure the flags are as expected.
# These values and resulting flags are 
# from Table 6.3, page 14, in LSDS-1619 Version 2.0 (L8 C2 L2 Product Guide)
l8_test_values1 =         [1, 21824, 21826, 21888, 21890, 22080, 22144, 22280, 23888, 23952]
l8_flag_values1 = \
 {'Fill' :                [1,      0,     0,     0,    0,      0,     0,     0,     0,    0],
'Dilated_Cloud' :         [0,      0,     1,     0,    1,      0,     0,     0,     0,    0],
'Cirrus' :                [0,      0,     0,     0,    0,      0,     0,     0,     0,    0],
'Cloud' :                 [0,      0,     0,     0,    0,      0,     0,     1,     0,    0],
'Cloud_Shadow' :          [0,      0,     0,     0,    0,      0,     0,     0,     1,    1],
'Snow' :                  [0,      0,     0,     0,    0,      0,     0,     0,     0,    0],
'Clear' :                 [0,      1,     1,     0,    0,      1,     0,     0,     1,    0],
'Water' :                 [0,      0,     0,     1,    1,      0,     1,     0,     0,    1],
'Cloud_Confidence' :      [0,      1,     1,     1,    1,      2,     2,     3,     1,    1],
'Cloud_Shadow_Confidence':[0,      1,     1,     1,    1,      1,     1,     1,     3,    3],
'Snow_Ice_Confidence' :   [0,      1,     1,     1,    1,      1,     1,     1,     1,    1],
'Cirrus_Confidence' :     [0,      1,     1,     1,    1,      1,     1,     1,     1,    1]}
 
 
# take the lists above, which are easy to write down and form, and convert
# into test cases to pass to the test function. 
# l8_test_cases format is [(qa_value, expected_result_dict), ...]
l8_test_cases = []
for test_i, test in enumerate(l8_test_values1):
    test_value_expected_output={}
    for flag, flag_values in l8_flag_values1.items():
        test_value_expected_output[flag] = np.array([flag_values[test_i]], dtype=np.uint8)
    l8_test_cases.append(('LANDSAT_8_C2_L2_QAPixel', test, test_value_expected_output))

# Landsat 4-7 SR_CLOUD_QA values from Table 5-4 in LSDS-1618 Version 3.0 (L4-7 C2 L2 Product Guide)
l47_test_values =   [0, 1, 2, 4, 8, 9, 12, 16, 20, 24, 32, 34, 36, 40, 48, 52, 56]
l47_flag_values = \
{'DDV' :            [0, 1, 0, 0, 0, 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
'Cloud' :           [0, 0, 1, 0, 0, 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0],
'Cloud_Shadow' :    [0, 0, 0, 1, 0, 0,  1,  0,  1,  0,  0,  0,  1,  0,  0,  1,  0],
'Adjacent_to_Cloud':[0, 0, 0, 0, 1, 1,  1,  0,  0,  1,  0,  0,  0,  1,  0,  0,  1],
'Snow' :            [0, 0, 0, 0, 0, 0,  0,  1,  1,  1,  0,  0,  0,  0,  1,  1,  1],
'Water' :           [0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1]}

l47_test_cases = []
for test_i, test in enumerate(l47_test_values):
    test_value_expected_output={}
    for flag, flag_values in l47_flag_values.items():
        test_value_expected_output[flag] = np.array([flag_values[test_i]], dtype=np.uint8)
    l47_test_cases.append(('LANDSAT_47_C2_L2_SRCloudQA', test, test_value_expected_output))


qa_test_cases = l8_test_cases + l47_test_cases

@pytest.mark.parametrize('product, test_qa_value, expected_output', qa_test_cases)
def test_confirm_flag_values(product, test_qa_value, expected_output):
    """Output should match known values above"""
    output = unpack_to_dict(test_qa_value, product=product, flags='all')
    assert output == expected_output

@pytest.mark.parametrize('product, test_qa_value, expected_output', qa_test_cases)
def test_confirm_wrong_flag_values(product, test_qa_value, expected_output):
    """Perturbe a single value to ensure wrong arrays are indeed caught"""
    output = unpack_to_dict(test_qa_value, product=product, flags='all')
    first_key = list(output.keys())[0]
    output[first_key] += 1
    assert output != expected_output
