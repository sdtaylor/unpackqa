from setuptools import setup, find_packages

# Package meta-data.
NAME = 'unpackqa'
DESCRIPTION = 'QA bit unpacking for Landsat, MODIS, Sentinal, VIIRS, and more.'
URL = 'https://github.com/sdtaylor/unpackqa'
AUTHOR = 'Shawn Taylor'
LICENSE = 'MIT'
REQUIRES_PYTHON = '>=3.6.0'

# What packages are required for this module to be executed?
REQUIRED = [
    'numpy',
    'pyyaml',
]

LONG_DESCRIPTION = """
# unpackqa
Methods for unpacking, labelling and masking all common remote sensing QA bands which are stored in bit-wise values.  

- Works with single QA values, 1D arrays (eg. time series), or 2D arrays (eg. full scenes).  
- Get a QA mask in a single line of code: `unpackqa.unpack_to_array(qa,'LANDSAT_8_C2_L2_QAPixel','Cloud')`
- The same methods are used for all sensors, with specific product flags specified via arguments.  
- No file reading or writing, everything is handled as pre-loaded arrays.  
- Requires python 3.6+, with numpy and pyyaml as the only dependencies.  

## Installation

Install via pip:

```
pip install unpackqa
```

## Documentation
[https://sdtaylor.github.io/unpackqa](https://sdtaylor.github.io/unpackqa)  
"""

version = {}
with open('unpackqa/version.py') as fp:
    exec(fp.read(), version)
VERSION = version['__version__']

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      url=URL,
      author=AUTHOR,
      license=LICENSE,
      packages=find_packages(),
      python_requires=REQUIRES_PYTHON,
      install_requires=REQUIRED,
      include_package_data=True,
      zip_safe=False)
