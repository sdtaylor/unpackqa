from .base import PackQABase
from .product_loader import all_products
from .tools.validation import validate_product_spec


def pack_from_dict(flag_values, product, flags='all', validate=True):
    """
    

    Parameters
    ----------
    qa : TYPE
        DESCRIPTION.
    product : TYPE
        DESCRIPTION.
    flags : TYPE, optional
        DESCRIPTION. The default is 'all'.

    Returns
    -------
    None.

    """
    if isinstance(product, dict):
        validate_product_spec(product)
        base = PackQABase(product, validate=validate)
        return base._pack_from_dict(flag_values, flags=flags)
    else:
        error_message  = 'product should be a dictionary.'
        raise TypeError(error_message)