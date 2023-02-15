from .base import PackQABase
from .product_loader import all_products
from .tools.validation import validate_product_spec



def pack_from_array(flag_values, product, flags='all', flag_axis=-1, validate=True):
    """
    Get a bitpacked QA array from an array of flag values.
    
    This is currently experimental. Tests for it work, but some use cases would be useful to validate it. 
    Open an issue on the github page if you have an interesting use case and would like to contribute. 
    
    `flag_values` should be a np.array where either the first (0) or last (-1) axis
    is the flag values. The resulting array will match the array shape minus 
    the flag axis.
    
    This reverses `unpack_to_array()` in that:  
        `qa_values == pack_from_array(unpack_to_array(qa_values))` is True
    
    All flags specified in `product` should have a corresponding location in 
    flag_values.

    Parameters
    ----------
    flag_values : np.array
        A numpy array of flag values. The flag axis (specifed via `flag_axis`) 
        needs to match the number of flags specified in `product`. 
        eg. `flag_values.shape[flag_axis] == len(product_info['flag_info'])` must
        be true.
        
    product : dict
        A custom bit flag specification may also be used via a dictionary.
        For example, below is an 8 bit qa flag where the 1st and 2nd flags are bits 0 and 1,
        and the 3rd flag is spread across bits 4 and 5. Note bit 3 is not specified
        so is ignored. `max_value` is generally set to the maximum possible
        value given the bit size. If this option is used then the `flags` 
        argument can be left as the default `all`.  
        Flags should be ordered from lowest to highest bits. The order of the mask axis
        in the returned array will be the same as the flag order specifed here. 
        
        ```
        product_info = {'flag_info':{'flag1_description':[0],
                                     'flag2_description':[1],
                                     'flag3_description':[4,5]},
                        'max_value' : 255,
                        'num_bits'  : 8}
        ```
    flags : list or str
        List of flags to pack, or `all` (the default) to pack all flags
        specified in `product`
    flag_axis : int, optional
        The location of the flag axis within the flag_values array. This defaults
        to -1 (the last position), which matches the output of unpack_to_array().
    validate : bool, optional
        Perform checks before bitpacking. Setting to false can speed this
        up slightly.

    Returns
    -------
    np.array
        A QA array with the same shape as `flag_values` minus the flag axis, and 
        with the dtype matching `num_bits` in `product` (either np.uint 8, 16, or 32).

    """
    if isinstance(product, dict):
        validate_product_spec(product)
        base = PackQABase(product, validate=validate)
        return base._pack_from_array(flag_values, flags=flags, flag_axis=flag_axis)
    else:
        error_message  = 'product should be a dictionary.'
        raise TypeError(error_message)

def pack_from_dict(flag_values, product, flags='all', validate=True):
    """
    Get a bitpacked QA array from an array of dictionary values.
    
    This is currently experimental. Tests for it work, but some use cases would be useful to validate it. 
    Open an issue on the github page if you have an interesting use case and would like to contribute. 

    flag_values should be a dict where the keys are flag names and match the
    flag names in `product`. The dictionary values should be corresponding
    flag array, and all arrays must have the same shape. The resulting
    bitpacked QA array will have the same  shape.

    This reverses `unpack_to_dict()` in that:  
        `qa_values == pack_from_dict(unpack_to_dict(qa_values))` is True
    
    All flags specified in `product` should have a corresponding location in 
    flag_values.


    Parameters
    ----------
    flag_values : dict
        A dictionary where the flag names are keys and values are np.arrays
        of the flag values. All entries must have the same shape.
    product : dict
        A custom bit flag specification may also be used via a dictionary.
        For example, below is an 8 bit qa flag where the 1st and 2nd flags are bits 0 and 1,
        and the 3rd flag is spread across bits 4 and 5. Note bit 3 is not specified
        so is ignored. `max_value` is generally set to the maximum possible
        value given the bit size. If this option is used then the `flags` 
        argument can be left as the default `all`.  
        Flags should be ordered from lowest to highest bits. The order of the mask axis
        in the returned array will be the same as the flag order specifed here. 
        
        ```
        product_info = {'flag_info':{'flag1_description':[0],
                                     'flag2_description':[1],
                                     'flag3_description':[4,5]},
                        'max_value' : 255,
                        'num_bits'  : 8}
        ```
    flags : list or str
        List of flags to pack, or `all` (the default) to pack all flags
        specified in `product`
    validate : bool, optional
        Perform checks before bitpacking. Setting to false can speed this
        up slightly.
    

    Returns
    -------
    np.array
        A QA array with the same shape as the arrays in `flag_values`, and 
        with dtype matching `num_bits` in `product` (either np.uint 8, 16, or 32).

    """
    if isinstance(product, dict):
        validate_product_spec(product)
        base = PackQABase(product, validate=validate)
        return base._pack_from_dict(flag_values, flags=flags)
    else:
        error_message  = 'product should be a dictionary.'
        raise TypeError(error_message)
