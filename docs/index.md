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

