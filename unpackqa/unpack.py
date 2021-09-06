from .base import UnpackQABase
from .product_loader import all_products
from .tools.validation import validate_product_spec

def unpack_to_array(qa, product, flags='all'):
    """
    Make a mask array with the same shape as qa with an additional axis
    for all flag masks.

    Parameters
    ----------
    qa : np.array or int
        An array of any shape with an int-like dtype. If a single integer 
        it will be coverted to a numpy array with length 1. 
    product : str or dict
        A unique product identifer string. See `list_products()` for availability.
        
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
        
    flags : list of strings or 'all', optional
        List of flags to return. If 'all', the default, then all available
        flags are returned in the array. See available flags for each 
        product with `list_qa_flags()`.

    Returns
    -------
    np.array
        If only a single flag is set then the array shape will be the same
        as qa.shape. If > 1 flag is set then an axis will be added in 
        position -1, with the shape as qa.shape + (n_flags,)
        Ordering of the flag axis will be the same order of the `flags` 
        list argument. 
        If `flags` is 'all' then the order is the same as that in 
        `available_qa_flags`, which are be aligned with the flag bit order.

    """
    if isinstance(product, dict):
        validate_product_spec(product)
        base = UnpackQABase(product)
        return base._unpack_to_array(qa, flags=flags)
    
    if product in all_products:
        product_info = all_products[product]
        base = UnpackQABase(product_info)
        return base._unpack_to_array(qa, flags=flags)
    else:
        error_message  = 'Unknown product: {}. Use list_products() for availability'
        raise ValueError(error_message.format(product))

def unpack_to_dict(qa, product, flags='all'):
    """
    Get mask arrays for the specified flags in a dictionary format.

    Parameters
    ----------
    qa : np.array or int
        An array of any shape with an int-like dtype. If a single integer 
        it will be coverted to a numpy array with length 1. 
    product : str or dict
        A unique product identifer string. See `list_products()` for availability.
        
        A custom bit flag specification may also be used via a dictionary.
        For example, below is an 8 bit qa flag where the 1st and 2nd flags are bits 0 and 1,
        and the 3rd flag is spread across bits 4 and 5. Note bit 3 is not specified
        so is assumed unused. `max_value` is generally set to the maximum possible
        value given the bit size. If this option is used then the `flags` 
        argument can be left as the default `all`.  
        Flags should be ordered from lowest to highest bits. The resulting dictionary
        key names will be the same as the flag descriptions specified here.
        
        ```
        product_info = {'flag_info':{'flag1_description':[0],
                                     'flag2_description':[1],
                                     'flag3_description':[4,5]},
                        'max_value' : 255,
                        'num_bits'  : 8}
        ```
        
    flags : list of strings or 'all', optional
        List of flags to return. If 'all', the default, then all available
        flags are returned in the array. See available flags for each 
        product with `list_qa_flags()`.

    Returns
    -------
    dict
        A dictionary where the flag names are keys and values are np.arrays
        of the flag mask with shape qa.shape. All entries will have the
        same shape.

    """
    if isinstance(product, dict):
        validate_product_spec(product)
        base = UnpackQABase(product)
        return base._unpack_to_dict(qa, flags=flags)
    
    if product in all_products:
        product_info = all_products[product]
        base = UnpackQABase(product_info)
        return base._unpack_to_dict(qa, flags=flags)
    else:
        error_message  = 'Unknown product: {}. Use list_products() for availability'
        raise ValueError(error_message.format(product))
