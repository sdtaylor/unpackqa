## Custom QA Specification

If you have a QA band that is not configured in this package you can manually specify how it should be unpacked. 

You can do this by setting up a dictionary with the following three entries:

- `flag_info`: another dictionary where each entry represents a single flag. Each key is the name of the the flag, with the value a list of the flags designated bits.
- `num_bits`: the number of bits in the flag. this is usually 8 or 16. 
- `max_value`: the maximum value expected in the QA band, this will usually be (2**num_bits)-1

The following example is an 8 bit QA band with 3 flags. Flags 1 and 2 are bits 0 and 1, flag 3 is spread across bits 4 and 5 (and thus can have the final values 0-3). 
Bits 3 and 6-8 are ignored. 

```

custom_product_info = {'flag_info':{'flag1_description':[0],
                                    'flag2_description':[1],
                                    'flag3_description':[4,5]},
                       'max_value' : 255,
                       'num_bits'  : 8}
```

This can now be used directly in the unpack functions. The `flags` argument can be left as the default, and all specified flags will be returned. In `unpack_to_array` the
order of the mask axis is the same as the flag order specified.

```
import numpy as np
import unpackqa
qa_array = np.array([[9,32],[9,2]])

mask_array = unpackqa.unpack_to_array(qa_array, product=custom_product_info)
qa_array.shape
(2, 2)
mask_array.shape                                                                                                                                                             
(2, 2, 3)
mask_array
array([[[1, 0, 0],
        [0, 0, 2]],

       [[1, 0, 0],
        [0, 1, 0]]], dtype=uint8)

```
With `unpack_to_dict` the resulting dictionary keys will be the flag names specified. 

```
mask_dict = unpackqa.unpack_to_dict(qa_array, product=custom_product_info) 
mask_dict
{'flag1_description': array([[1, 0],
                             [1, 0]], dtype=uint8),
 'flag2_description': array([[0, 0],
                             [0, 1]], dtype=uint8),
 'flag3_description': array([[0, 2],
                             [0, 0]], dtype=uint8)}

```

## Notes  
- the `flag_info` entries should be orderd from lowest to highest bit.
- Flag descriptions should be short, not start with numbers, and not contain spaces or any special characters (underscores are ok). 
While unpackqa will not object to any of those, it is easy for the descriptions to end up as column names in data.frames where they 
can be difficult to work with if spaces, leading numbers, etc. are included. 
- bit entries cannot be empty, negative, or exceed `num_bits`. For example all the following bit entries are invalid.

```
product_info = {'flag_info':{'flag1_description':[],
                             'flag2_description':[-1],
                             'flag3_description':[12]},
                'max_value' : 255,
                'num_bits'  : 8}
```
- Invalid custom specification will raise the error `unpackqa.InvalidProductSpec`
