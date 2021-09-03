import pytest
import numpy as np

from unpackqa import (unpack_to_array,
                        unpack_to_dict, 
                        list_products,
                        list_qa_flags
                        )


"""
Just iterating thru all products as integration tests.
"""

qa_array = np.array([[8,8,8],
                     [16,16,16],
                     [255,255,255]])

all_product_identifiers = list_products(sensor='all')

@pytest.mark.parametrize('product', all_product_identifiers)
def test_unpack_array_shape(product):
    """ 
    With >1 flag unpack_to_array result should match the input shape and have
    a new axis at position (-1) with the same length as number of flags.
    """
    n_flags = len(list_qa_flags(product = product))
    target_shape = qa_array.shape + (n_flags,)
    
    result = unpack_to_array(qa_array, product = product)
    assert result.shape == target_shape

@pytest.mark.parametrize('product', all_product_identifiers)
def test_single_flag_array_shape(product):
    """
    A single flag should return an array the same shape as the input and
    *not* have an added axis.
    """
    flags = list_qa_flags(product = product)
    flags = [flags[0]]
    result = unpack_to_array(qa_array, product = product, flags=flags)
    
    assert result.shape == qa_array.shape

@pytest.mark.parametrize('product', all_product_identifiers)
def test_unpack_dict_shape(product):
    """Each dictionary value in unpack_to_dick should match the input qa shape"""
    flags = list_qa_flags(product = product)
    target_shape = qa_array.shape
    
    result = unpack_to_dict(qa_array, product = product, flags='all')
    
    all_shapes_good = [result[flag].shape == target_shape for flag in flags]
    assert all(all_shapes_good)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_unpack_dict_all_flags(product):
    """ The all flag indicator returns all available flags"""
    flags = list_qa_flags(product = product)
    
    result = unpack_to_dict(qa_array, product = product, flags='all')
    all_flags_in_result = [f in result for f in flags]
    all_results_in_flags = [f in flags for f in result.keys()]
    assert all(all_flags_in_result) and all(all_results_in_flags)
    
@pytest.mark.parametrize('product', all_product_identifiers)
def test_unpack_dict_2_flags1(product):
    """ Get the first and last flag only. """
    flags = list_qa_flags(product = product)
    flags = [flags[0], flags[-1]]
    
    result = unpack_to_dict(qa_array, product = product, flags=flags)
    all_flags_in_result = [f in result for f in flags]
    all_results_in_flags = [f in flags for f in result.keys()]
    assert all(all_flags_in_result) and all(all_results_in_flags)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_unpack_dict_2_flags2(product):
    """ Get the first flag only. """
    flags = list_qa_flags(product = product)
    flags = [flags[0]]
    
    result = unpack_to_dict(qa_array, product = product, flags=flags)
    all_flags_in_result = [f in result for f in flags]
    all_results_in_flags = [f in flags for f in result.keys()]
    assert all(all_flags_in_result) and all(all_results_in_flags)

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_wrong_axis_ordering(product):
    """
    Ordering of the flag axis is the same as the flag list. 
    When the flag list is reversed, the resulting arrays should not match.
    """
    flags = list_qa_flags(product = product)
    
    mask1 = unpack_to_array(qa_array, product=product, flags=flags)
    flags.reverse()
    mask2 = unpack_to_array(qa_array, product=product, flags=flags)
    
    assert not (mask1 == mask2).all()

@pytest.mark.parametrize('product', all_product_identifiers)
def test_flag_correct_axis_ordering(product):
    """
    Ordering of the flag axis is the same as the flag list. 
    When the flag list is reversed, the resulting arrays should not match.
    But should match when the axis is flipped back again.
    """
    flags = list_qa_flags(product = product)
    
    mask1 = unpack_to_array(qa_array, product=product, flags=flags)
    flags.reverse()
    mask2 = unpack_to_array(qa_array, product=product, flags=flags)
    
    assert (mask1 == np.flip(mask2, axis=-1)).all()