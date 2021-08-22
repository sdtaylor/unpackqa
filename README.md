# pyUnpackQA  
Methods for unpacking and labelling all common remote sensing QA bands which are stored in bit-wise values.  

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (eg. full scenes).  
- The same methods are used for all sensors, with specific product flags specified via arguments.  
- No file reading or writing, everything is handled as pre-loaded arrays.  
- Requires python 3.6+, with numpy and pyyaml as the only dependencies.  

## Installaion

Install via pip directly from the github repo:

```
pip install git+git://github.com/sdtaylor/pyUnpackQA
```

## Documentation
[https://sdtaylor.github.io/pyUnpackQA](https://sdtaylor.github.io/pyUnpackQA)  

## Quickstart

```
import numpy as np
from pyUnpackQA import unpack_to_array

# Specify the Landsat 8 Collection 2 Level 2 QA Pixel
# see all identifiers in pyUnpackQA.list_products()
l8_identifer = 'L8C2L2_QAPixel'

qa_array = np.array([[21284,0],[21284,0]])

unpack_to_array(qa_array, product = l8_identifer)
array([[[0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

       [[0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]], dtype=uint8)

# The original shape is retained, with a new axis for the 
# 12 Landsat 8 QA flags. 
qa_array.shape
(2,2)
unpack_to_array(qa_array, product = l8_identifer).shape
(2,2,12)

# Masks for individual flags can also be obtained from a dictionary object
from pyUnpackQA import unpack_to_dict

# See flags for each product with pyUnpackQA.list_qa_flags()
flags = ['Cloud','Cloud Shadow']

flag_masks = unpack_to_dict(qa_array, product = l8_identifer, flags=flags)
flag_masks['Cloud'].shape
(2,2)
flag_masks['Cloud Shadow'].shape
(2,2)

```
