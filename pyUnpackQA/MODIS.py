from collections import OrderedDict

from .base import Base

class MOD13Q1v006_DetailedQA(Base):
    """
    MODIS/Terra Vegetation Indices 16-Day L3 Global 250m
    
    References doc: MODIS Vegetation Index User’s Guide (MOD13 Series)
                        Version 3.00, June 2015 (Collection 6)
                    https://lpdaac.usgs.gov/products/mod13q1v006/

    
    Confirmed products:
        Google Earth Engine: MODIS/006/MOD13Q1
        AWS Store XXXXX
    """
    def __init__(self):
        self.flag_info = OrderedDict({'VI Quality' : [0,1],
                                      'VI Usefulness': [2,3,4,5],
                                      'Aerosol Quantity' : [6,7],
                                      'Adjacent cloud detected': [8],
                                      'Atmosphere BRDF Correction': [9],
                                      'Mixed Clouds': [10],
                                      'Land/Water Mask': [11,12,13],
                                      'Possible snow/ice': [14],
                                      'Possible shadow': [15]})
        
        self.num_bits = 16
        self.max_value = 65534

#TODO: I don't think summaryQA is atually bit packed. 
class MOD13Q1v006_SummaryQA(Base):
    """
    *********Dont think I actually need 
    MODIS/Terra Vegetation Indices 16-Day L3 Global 250m
    
    Only 2 bits are used for this QA band, so the resulting values are:
        
    0: Good data, use with confidence
    1: Marginal data, useful but look at detailed QA for more information
    2: Pixel covered with snow/ice
    3: Pixel is cloudy

    
    References doc: MODIS Vegetation Index User’s Guide (MOD13 Series)
                        Version 3.00, June 2015 (Collection 6)
                    https://lpdaac.usgs.gov/products/mod13q1v006/
    
    Confirmed products:
        Google Earth Engine: MODIS/006/MOD13Q1
        AWS Store XXXXX
    """
    def __init__(self):
        self.flag_info = OrderedDict({'VI Quality' : [0,1]})
        
        self.num_bits = 8


#---------------
# MOD13Q1v006 and MOD13A1v006 share the same QA properties. The only difference
# is their pixel resolution (250 vs 500m). 
# So MOD13A1v006 can just inheret MOD13Q1v006. 
#---------------
class MOD13A1v006_DetailedQA(MOD13Q1v006_DetailedQA):
    """
    MODIS/Terra Vegetation Indices 16-Day L3 Global 500m
    
    References doc: MODIS Vegetation Index User’s Guide (MOD13 Series)
                        Version 3.00, June 2015 (Collection 6)
                    https://lpdaac.usgs.gov/products/mod13q1v006/

    
    Confirmed products:
        Google Earth Engine: MODIS/006/MOD13A1
        AWS Store XXXXX
    """
    pass

class MOD13A1v006_SummaryQA(MOD13Q1v006_SummaryQA):
    """
    MODIS/Terra Vegetation Indices 16-Day L3 Global 500m
    
    Only 2 bits are used for this QA band, so the resulting values are:
        
    0: Good data, use with confidence
    1: Marginal data, useful but look at detailed QA for more information
    2: Pixel covered with snow/ice
    3: Pixel is cloudy

    
    References doc: MODIS Vegetation Index User’s Guide (MOD13 Series)
                        Version 3.00, June 2015 (Collection 6)
                    https://lpdaac.usgs.gov/products/mod13q1v006/
    
    Confirmed products:
        Google Earth Engine: MODIS/006/MOD13A1
        AWS Store XXXXX
    """
    pass