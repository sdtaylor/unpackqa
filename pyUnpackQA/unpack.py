from .base import UnpackQABase
from .product_loader import all_products

def unpack_to_array(qa, product, flags='all'):
    """
    Make a mask array with the same shape as qa with an additional axis
    for all flag masks.

    Parameters
    ----------
    qa : np.array or int
        An array of any shape with an int-like dtype. If a single integer 
        it will be coverted to a numpy array with length 1. 
    product : str
        A unique product identifer. See list_products() for availability.
    flags : list of strings or 'all', optional
        List of flags to return. If 'all', the default, then all available
        flags are returned in the array. See available flags for each 
        product with `list_qa_flags()`.

    Returns
    -------
    np.array
        Flag array with shape qa.shape + (n_flags,). Flag order will be 
        the same order of the `flags` list argument. If `flags` is 'all' 
        then the order is the same as that in `available_qa_flags`, which
        will be aligned with the flag bit order.

    """
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
    product : str
        A unique product identifer. See list_products() for availability.
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
    if product in all_products:
        product_info = all_products[product]
        base = UnpackQABase(product_info)
        return base._unpack_to_dict(qa, flags=flags)
    else:
        error_message  = 'Unknown product: {}. Use list_products() for availability'
        raise ValueError(error_message.format(product))