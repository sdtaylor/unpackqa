import ee
from gee_subset.gee_subset import gee_subset
import pandas as pd
import seaborn as sns
import numpy as np
# ee.Authenticate()
ee.Initialize()

import unpackqa


# The MODIS vegetation product has a Summary QA band which has 4 values:
#    0: Good data, use with confidence
#    1: Marginal data, useful but look at detailed QA for more information
#    2: Pixel covered with snow/ice
#    3: Pixel is cloudy
# It also a a DetailedQA band which is bit packed and gives more information about
# the pixel quality. Here we'll unpack the DetailedQA band to see. 

# This uses the gee_subset packge to query Google Earth Engine (GEE) for a single
# pixel timeseries across ~20 years. To use it you'll need a GEE account.
# - [GEE Info](https://developers.google.com/earth-engine/python_install)
# - [gee_subset package](https://github.com/bluegreen-labs/gee_subset)


df = gee_subset(product    = 'MODIS/006/MOD13A1',
                bands      = ['NDVI','DetailedQA'],
                scale      = 500,
                start_date = '2015-01-01',
                end_date   = '2020-12-31',
                latitude   =   44.8166,
                longitude  = -114.8177,
                pad        =  0)

# Adjust NDVI by the scaling factor and drop any NA values
df['NDVI'] = df.NDVI * 0.0001
df = df[~df.NDVI.isna()].reset_index()

# unpackqa only works on integers. Here DetailedQA are 16-bits
df['DetailedQA'] = df.DetailedQA.astype(np.uint16)

expanded_detailed_qa = unpackqa.unpack_to_dict(df.DetailedQA.values, product = 'MOD13Q1v006_DetailedQA', flags='all')

# This produces a dictionary where each key is a flag, and each value is an 
# array the same length as the df data.frame
# This can be converted directly to a new data.frame where the columsn are the flags,
# and then appended to the original data.frame.
expanded_detailed_qa = pd.DataFrame(expanded_detailed_qa)
df = pd.concat([df, expanded_detailed_qa], axis=1)

# each pixel value in the time series now has the associated flags as columns.
# The VI_Quality flag has 3 values, where 0 signifies the best quality, 1 signifies a QA issue, and 2 indicates likely clouds. 
colors = {0:'green',
          1:'red',
          2:'darkred'}

sns.scatterplot(x='date',y='NDVI',hue='VI_Quality',data=df,palette=colors)
