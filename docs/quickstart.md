# Quickstart

## Listing available sensor, flags, and products.
`unpackqa.list_sensors()`,`unpackqa.list_products()`  
These list the available sensors and sensor data products, respectively. By default they list everything configured in the package. 

`unpackqa.list_qa_flags()`
This lists the flags which are parsed from the QA bits. These match the Flag Name column in the product description tables. A product name must be specified here. For example:

```
import numpy as np
import unpackqa

unpackqa.list_qa_flags('LANDSAT_8_C2_L2_QAPixel')

['Fill',
 'Dilated_Cloud',
 'Cirrus',
 'Cloud',
 'Cloud_Shadow',
 'Snow',
 'Clear',
 'Water',
 'Cloud_Confidence',
 'Cloud_Shadow_Confidence',
 'Snow_Ice_Confidence',
 'Cirrus_Confidence']
```

## Unpacking to an array
`unpackqa.unpack_to_array(qa, product='LANDSAT_8_C2_L2_QAPixel', flags='all')`  
This will return the QA values of a numpy array or integer. The returned value will have an entry for all flags listed in the `flags` argument. By default `flags` is `all` which will return all flags listed in `list_qa_flags()`.

```
unpackqa.unpack_to_array(21284, product='LANDSAT_8_C2_L2_QAPixel')
array([[0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 1]], dtype=uint8)

qa_array = np.array([[21284,0],[21284,0]])
qa_array.shape
(2,2)
unpackqa.unpack_to_array(qa_array, product='LANDSAT_8_C2_L2_QAPixel').shape
(2,2,12)
```

## Unpacking to a dictionary
`unpackqa.unpack_to_dict(qa, product='LANDSAT_8_C2_L2_QAPixel', flags='all')`  
This is similar to `unpack_to_array`, but instead of a stacked array for all flags, it returns a dictionary where the keys are the flag names, and the value for each key is the flag array. The shape of each array is the same as the input qa.shape. This is usefull when single pixels or time series of pixels are being used, as this can be put directly into a pandas DataFrame.

```
qa_array = np.array([56598, 56598,0,0,56598])
unpackqa.unpack_to_dict(qa_array, product='LANDSAT_8_C2_L2_QAPixel')
{'Fill': array([0, 0, 0, 0, 0], dtype=uint8),
 'Dilated_Cloud': array([1, 1, 0, 0, 1], dtype=uint8),
 'Cirrus': array([1, 1, 0, 0, 1], dtype=uint8),
 'Cloud': array([0, 0, 0, 0, 0], dtype=uint8),
 'Cloud_Shadow': array([1, 1, 0, 0, 1], dtype=uint8),
 'Snow': array([0, 0, 0, 0, 0], dtype=uint8),
 'Clear': array([0, 0, 0, 0, 0], dtype=uint8),
 'Water': array([0, 0, 0, 0, 0], dtype=uint8),
 'Cloud_Confidence': array([1, 1, 0, 0, 1], dtype=uint8),
 'Cloud_Shadow_Confidence': array([3, 3, 0, 0, 3], dtype=uint8),
 'Snow_Ice_Confidence': array([1, 1, 0, 0, 1], dtype=uint8),
 'Cirrus_Confidence': array([3, 3, 0, 0, 3], dtype=uint8)}

unpackqa.unpack_to_dict(qa_array, product='LANDSAT_8_C2_L2_QAPixel')['Cloud'].shape
(5,)
```
