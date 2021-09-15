from collections import OrderedDict
import numpy as np

from .tools.unpackbits import unpackbits, packbits

class UnpackQABase:
    """
    Generalized bit unpacking methods. 
    """
    def __init__(self, product_info):
        self.flag_info = product_info['flag_info']
        self.num_bits = product_info['num_bits']
        self.max_value = product_info['max_value']

    def _parse_flag_args(self, passed_flags):
        if passed_flags == 'all':
            passed_flags = self._available_qa_flags()
        elif isinstance(passed_flags, list) and len(passed_flags) > 0:
            valid_flags = self._available_qa_flags()
            if not all([f in valid_flags for f in passed_flags]):
                raise ValueError('Invalid flag name passed')
        else:
            error_message = "flags should be a list of strings or 'all'"
            raise ValueError(error_message)
        
        return passed_flags
    
    def _validate_arr(self, arr):
        if not isinstance(arr, np.ndarray):
            raise TypeError('qa should be a numpy int-like array. ' + \
                            'If a single value then it should be type int')
        
        if not np.issubdtype(arr.dtype, np.integer):
            raise TypeError('qa should be an int-like array.' + \
                            'Transform via qa.astype(np.int32)')
        
        if arr.max() > self.max_value:
            m = arr.max()
            error_message = 'qa has values larger than the specified range for this product. ' + \
                            'max value was {} and the valid range is 0-{}'
            raise ValueError(error_message.format(m, self.max_value))
        
        if arr.min() < 0:
            m = arr.min()
            error_message = 'qa has values smaller than the specified range for this product. ' + \
                            'min value was {} and the valid range is 0-{}'
            raise ValueError(error_message.format(m, self.max_value))
    
    def _available_qa_flags(self):
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
    
    def _unpack_array_core(self, qa, flags):
        """
        The core function for converting the qa array to flag masks. 
        This returned value here is adjusted slightly based on whether its being 
        returned as a single array (unpack_to_array) or as a dictionary
        of arrays (unpack_to_dict)

        Parameters
        ----------
        qa : np.array or int
            An array of any shape with an int-like dtype. If a single integer 
            it will be coverted to a numpy array with length 1. 
        flags : list of strings or 'all', optional
            List of flags to return. 

        Returns
        -------
        np.array
            Flag array with shape (n_flags,) + qa.shape. Flag order will be 
            the same order of the `flags` list argument. 

        """       
        # allow a non-array if it's a single integer. It must still pass
        # other checks though.
        if isinstance(qa, int):
            qa = np.array([qa], dtype=np.int32)
        
        self._validate_arr(qa)
        
        bits = unpackbits(qa, num_bits = self.num_bits)
        
        n_flags = len(flags)
        mask_array = np.empty(shape = (n_flags,) + qa.shape, dtype=np.uint8)
        for flag_i, flag in enumerate(flags):
            flag_bit_locs = self.flag_info[flag]
            mask_array[flag_i] = self._get_single_flag_mask(bits, flag_bit_locs)
        
        return mask_array
    
    def _unpack_to_array(self, qa, flags='all'):
        """
        Return a numpy array of mask values. 

        Parameters
        ----------
        qa : np.array or int
            An array of any shape with an int-like dtype. If a single integer 
            it will be coverted to a numpy array with length 1. 
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
        flags = self._parse_flag_args(flags)
        flag_array = self._unpack_array_core(qa = qa, flags = flags)
        
        # If a single flag was passed return the original array shape
        # instead of an added axis of length 1.
        # If > 1 flag put the mask at the end since "adding" an axis is
        # more intuitive that way.
        if len(flags) == 1:
            flag_array = flag_array[0]
        else:
            flag_array = np.moveaxis(flag_array, source = 0, destination = -1)
        return flag_array
    
    def _unpack_to_dict(self, qa, flags='all'):
        """
        Get mask arrays for the specified flags in a dictionary format.

        Parameters
        ----------
        qa : np.array or int
            An array of any shape with an int-like dtype. If a single integer 
            it will be coverted to a numpy array with length 1. 
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
        flags = self._parse_flag_args(flags)
        flag_array = self._unpack_array_core(qa = qa, flags = flags)
        return {flag:flag_array[flag_i] for flag_i, flag in enumerate(flags)}


class PackQABase:
    """
    Generalized bit packing methods. 
    """
    def __init__(self, product_info, validate):
        self.flag_info = product_info['flag_info']
        self.num_bits = product_info['num_bits']
        self.max_value = product_info['max_value']
        self.validate  = validate

    def _parse_flag_args(self, passed_flags):
        if passed_flags == 'all':
            passed_flags = self._available_qa_flags()
        elif isinstance(passed_flags, list) and len(passed_flags) > 0:
            valid_flags = self._available_qa_flags()
            if not all([f in valid_flags for f in passed_flags]):
                raise ValueError('Invalid flag name passed')
        else:
            error_message = "flags should be a list of strings or 'all'"
            raise ValueError(error_message)
        
        return passed_flags
    
    def _validate_flag_array(self, flag_array):
        n_flags = len(self.flag_info)
        if flag_array.shape[0] != n_flags:
            msg = 'flag_array axis length ({}) must match number of flags ({})'
            raise ValueError(error_message.forma(flag_array.shape[0], n_flags))
            
        if flag_array.min() < 0:
            m = flag_array.min()
            msg = 'flag_array values smaller than the specified range for this product. ' + \
                  'min value was {} and the valid range is 0-{}'
            raise ValueError(error_message.format(m, self.max_value))
            
        for flag_i, (flag_name, flag_bit_locs) in enumerate(self.flag_info.items()):
            max_value = (2**len(flag_bit_locs)) - 1
            if flag_array[flag_i].max() > max_value:
                m = flag_array[flag_i].max()
                n_bits = len(flag_bit_locs)
                msg = 'axis for "{}" has values larger than larger than specified ' + \
                      'bit allows. max_value: {} for {} bits.'
                raise ValueError(msg.format(flag_name, m, n_bits))
                
        #TODO: if some bits are not specified in product, ensure they equal 0

    def _available_qa_flags(self):
        """
        A list of available QA flags for this product. 

        Returns
        -------
        list
            List of strings

        """
        return list(self.flag_info.keys())    
    
    def _pack_array_core(self, flag_array, flags):
        """
        

        Parameters
        ----------
        flag_array : TYPE
            DESCRIPTION.
        flags : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if self.validate:
            self._validate_flag_array(flag_array)
        #---
        # First convert the flag values, which are usually 0-1 but can also
        # be 0-3 (2 bits) or even 0-15 (4 bits), to the bit (0/1) values.
        # These are ordered by the bit location defined in the product_spec
        #---
        # bit_array shape is the same, but axis 0 is now the bit array with
        # length num_bits 
        # eg. (12,1024,1024) is a 1024x1024 array with 12 flags. 16 bits are needed
        # to store that many, so it ends up as (16,1024,1024)
        bit_shape = (self.num_bits,) + flag_array.shape[1:]
        bit_array = np.zeros(bit_shape, dtype=np.uint8)
        
        for flag_i, flag_name in enumerate(flags):
            flag_bit_locs = self.flag_info[flag_name]
            if len(flag_bit_locs) == 1:
                bit_array[flag_bit_locs[0]] = flag_array[flag_i]
            else:
                # > 1 bit flag means the flag values need conversion back
                # to 0/1. eg. [1,2,3] -> [[0,1],[1,0],[1,1]]
                bit_array[flag_bit_locs] = unpackbits(
                    flag_array[flag_i], 
                    num_bits = len(flag_bit_locs)
                    )
                
        return packbits(bit_array, num_bits=self.num_bits)

    def _pack_from_array(self, flag_values, flag_axis, flags='all'):
        """
        Get a qa array from a flag array.
        
        Parameters
        ----------
        flag_values : np.array
            numpy array of flag values.
        flags : TYPE, optional
            
            DESCRIPTION. The default is 'all'.
        flag_axis: int
            The location of the flag axis in flag_values.

        Returns
        -------
         np.array
            An array of qa values derived from bit packing individual flags.
            Shape is the same as the arrays in flag_values..

        """
        if flag_axis != 0:
            flag_values = np.moveaxis(
                flag_values, 
                source=flag_axis,
                destination=0)
            
        flags = self._parse_flag_args(flags)
        return self._pack_array_core(flag_array = flag_values, flags = flags)

    def _pack_from_dict(self, flag_values, flags='all'):
        """
        Get a qa array from flags in a dictionary

        Parameters
        ----------
        flag_values : dict
            A dictionary where the flag names are keys and values are np.arrays
            of the flag mask with shape qa.shape. All entries must have the
            same shape.
        flags : list of strings or 'all', optional
            List of flags to return. If 'all', the default, then all available
            flags are returned in the array. See available flags for each 
            product with `list_qa_flags()`.

        Returns
        -------
        np.array
            An array of qa values derived from bit packing individual flags.
            Shape is the same as the arrays in flag_values.

        """
        flags = self._parse_flag_args(flags)
        flags_present = [f in flag_values for f in flags]
        if not all(flags_present):
            raise ValueError('flag entries missing from flag_values dict')
        
        # stack the dictionary into a single array. ordered by product spec
        n_flags = len(flags)
        flag_value_shape = (n_flags,) + flag_values[flags[0]].shape
        flag_value_dtype = flag_values[flags[0]].dtype
        
        flag_array = np.zeros(flag_value_shape, dtype=flag_value_dtype)
        
        for flag_i, flag_name in enumerate(flags):
            flag_array[flag_i] = flag_values[flag_name]       
        
        return self._pack_array_core(flag_array = flag_array, flags = flags)