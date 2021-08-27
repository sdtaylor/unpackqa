# pyUnpackQA [![test-package](https://github.com/sdtaylor/pyUnpackQA/actions/workflows/test-package.yml/badge.svg)](https://github.com/sdtaylor/pyUnpackQA/actions/workflows/test-package.yml) 
Methods for unpacking, labelling, and masking for all common remote sensing QA bands which are stored in bit-wise values.  

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (eg. full scenes).  
- Get a QA mask in a single line of code: `pyunpackQA.unpack_to_array(qa,'LANDSAT_8_C2_L2_QAPixel','Cloud')`
- The same methods are used for all sensors, with specific product flags specified via arguments.  
- No file reading or writing, everything is handled as pre-loaded arrays.  
- Requires python 3.6+, with numpy and pyyaml as the only dependencies.  

# Installation

Install via pip directly from the github repo:

```
pip install git+git://github.com/sdtaylor/pyUnpackQA
```

