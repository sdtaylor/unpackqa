# unpackqa [![test-package](https://github.com/sdtaylor/unpackqa/actions/workflows/test-package.yml/badge.svg)](https://github.com/sdtaylor/unpackqa/actions/workflows/test-package.yml) 
A python package for QA/QC bit unpacking and labeling in earth science data products  

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (eg. full scenes).  
- Get a QA mask in a single line of code: `unpackqa.unpack_to_array(qa,'LANDSAT_8_C2_L2_QAPixel','Cloud')`
- The same methods are used for all sensors, with specific product flags specified via arguments.  
- Common data products are included. Specifying bit flag information manually is also supported.  
- No file reading or writing, everything is handled as pre-loaded arrays.  
- Requires python 3.6+, with numpy and pyyaml as the only dependencies.  

## Installation

Install via pip:

```
pip install unpackqa
```

## Documentation
[https://sdtaylor.github.io/unpackqa](https://sdtaylor.github.io/unpackqa)  

## Quickstart

```
import numpy as np
from unpackqa import unpack_to_array

# Specify the Landsat 8 Collection 2 Level 2 QA Pixel
# see all identifiers in unpackqa.list_products()
l8_identifer = 'LANDSAT_8_C2_L2_QAPixel'

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
from unpackqa import unpack_to_dict

# See flags for each product with unpackqa.list_qa_flags()
flags = ['Cloud','Cloud Shadow']

flag_masks = unpack_to_dict(qa_array, product = l8_identifer, flags=flags)
flag_masks['Cloud'].shape
(2,2)
flag_masks['Cloud Shadow'].shape
(2,2)

```
