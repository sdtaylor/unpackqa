# pyUnpackQA  
Methods for unpacking all common remote sensing QA bands which are stored in bit-wise values.  

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (full scenes).  
- The same methods are used for all sensors, with specific product flags specified via arguments.  
- No file reading or writing, everything is handled as pre-loaded arrays.  
- Requires python 3.6+, with numpy as the only dependecy. 

## Installaion

Install via pip directly from the github repo:

```
pip install git+git://github.com/sdtaylor/pyUnpackQA
```

## Documentation
[https://sdtaylor.github.io/pyUnpackQA/](https://sdtaylor.github.io/pyUnpackQA/)  

## Quickstart

```
import numpy as np
from pyUnpackQA.Landsat import L8C2L2_QAPixel
L8 = L8C2L2_QAPixel()

qa_array = np.array([[21284,0],[21284,0]])

L8.unpack_to_array(qa_array)
array([[[0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],

       [[0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]], dtype=uint8)

qa_array.shape
(2,2)
L8.unpack_to_array(qa_array).shape
(2,2,12)
```
