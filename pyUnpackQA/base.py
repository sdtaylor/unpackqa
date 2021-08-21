from collections import OrderedDict
import numpy as np

from tools.unpackbits import unpackbits

class Base():
    """
    Landsat 8 Collection 2 Level 2 QA Pixel unpacking.
    
    References doc: LSDS-1328 Version 6.0, September 2020
    
    Confirmed products:
        Google Earth Engine XXXXX
        AWS Store XXXXX
    """
    def __init__(self):
        self.flag_info = {}
        self.n_bits = 16
        
    def _parse_flag_args(self, passed_flags):
        if passed_flags == 'all':
            passed_flags = self.available_qa_flags()
        else:
            valid_flags = self.available_qa_flags()
            if not all([f in valid_flags for f in passed_flags]):
                raise ValueError('Invalid flag name passed')        
        return passed_flags
    
    def available_qa_flags(self):
        """
        A list of available QA flags for this product. 

        Returns
        -------
        list
            List of strings

        """
        return list(self.flag_info.keys())    
    
    def _get_single_flag_mask(self, bit_array, bit_location):
        """
        Internal function. Pull a specific mask from the full array, 
        converting multi-bit flags as neccessary.

        Parameters
        ----------
        bit_array : np.array
            The bit array where the 0 axis is bit locations
        bit_location : list of ints
            List of bit locations. These are described in the 'flag_info'
            dictionaries. 

        Returns
        -------
        np.array

        """
        if len(bit_location) == 1:
            # When a flag is just 1 bit then it's just 0 or 1
            return bit_array[bit_location[0]]
        else:
            # When a flag is > 1 bit then pack it to it's final value
            return np.packbits(bit_array[bit_location], axis=0, bitorder='little')
    
    def unpack_to_array(self, qa, flags='all'):
        """
        Make a mask array with the same shape as qa with an additional axis
        for all flag masks.

        Parameters
        ----------
        qa : np.array
            An array of any shape with an int-like dtype.
        flags : list of strings, optional
            List of flags to return. If 'all', the default, then all available
            flags are returned in the array. See available flags for each 
            product with `available_qa_flags`.

        Returns
        -------
        np.array
            Flag array with shape qa.shape + (n_flags,). Flag order will be 
            the same order of the `flags` list argument. If `flags` is 'all' 
            then the order is the same as that in `available_qa_flags`, which
            will be aligned with the flag bit order.

        """
        flags = self._parse_flag_args(flags)
        
        bits = unpackbits(qa, num_bits = self.num_bits)
        # put the bit axis in front for easier indexing
        bits = np.moveaxis(bits, source =  -1, destination = 0)
        
        n_flags = len(flags)
        mask_array = np.empty(shape = (n_flags,) + qa.shape, dtype=np.uint8)
        for flag_i, flag in enumerate(flags):
            flag_bit_locs = self.flag_info[flag]
            mask_array[flag_i] = self._get_single_flag_mask(bits, flag_bit_locs)
        
        # put the mask at the end since "adding" an axis is
        # more intuitive that way
        return np.moveaxis(mask_array, source = 0, destination = -1)
    
    def unpack_to_dict(self, qa, flags='all'):
        """
        Get mask arrays for the specified flags in a dictionary format.

        Parameters
        ----------
        qa : np.array
            An array of any shape with an int-like dtype.
        flags : list of strings, optional
            List of flags to return. If 'all', the default, then all available
            flags are returned in the array. See available flags for each 
            product with `available_qa_flags`.

        Returns
        -------
        dict
            A dictionary where the flag names are keys and values are np.arrays
            of the flag mask with shape qa.shape. All entries will have the
            same shape.

        """
        flags = self._parse_flag_args(flags)
        flag_array = self.unpack_to_array(qa = qa, flags = flags)
        flag_array = np.moveaxis(flag_array, source =  -1, destination = 0)
        return {flag:flag_array[flag_i] for flag_i, flag in enumerate(flags)}