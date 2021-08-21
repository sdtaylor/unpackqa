from collections import OrderedDict

from .base import Base

class L8C2L2_QAPixel(Base):
    """
    Landsat 8 Collection 2 Level 2 QA Pixel unpacking.
    
    References doc: LSDS-1328 Version 6.0, September 2020
    
    Confirmed products:
        Google Earth Engine: LANDSAT/LC08/C02/T1_L2
        AWS Store XXXXX
    """
    def __init__(self):
        self.flag_info = OrderedDict({'Fill' : [0],
                                      'Dilated Cloud': [1],
                                      'Cirrus' : [2],
                                      'Cloud': [3],
                                      'Cloud Shadow': [4],
                                      'Snow': [5],
                                      'Clear': [6],
                                      'Water': [7],
                                      'Cloud Confidence': [8,9],
                                      'Cloud Shadow Confidence': [10,11],
                                      'Snow/Ice Confidence': [12,13],
                                      'Cirrus Confidence': [14,15]})
        
        self.num_bits = 16
        
        
class L8C2L2_QARADSAT(Base):
    """
    Landsat 8 Collection 2 Level 2 QA RADSAT unpacking.
    aka. Radiometric Saturation and Terrain Occlusion QA
    
    For band saturation:
        0 = no saturation
        1 = saturated data
        
    For terrain occlusion:
        0 = no terrain occlusion
        1 = terrain occlusion
    
    References doc: LSDS-1328 Version 6.0, September 2020
    
    Confirmed products:
        Google Earth Engine: LANDSAT/LC08/C02/T1_L2
        AWS Store XXXXX
    """
    def __init__(self):
        self.flag_info = OrderedDict({'Band 1 Data Saturation' : [0],
                                      'Band 2 Data Saturation' : [1],
                                      'Band 3 Data Saturation' : [2],
                                      'Band 4 Data Saturation' : [3],
                                      'Band 5 Data Saturation' : [4],
                                      'Band 6 Data Saturation' : [5],
                                      'Band 7 Data Saturation' : [6],
                                     # bit 7 unused
                                      'Band 9 Data Saturation' : [8],
                                     # bit 9 unused
                                     # bit 10 unused
                                      'Terrain occlusion'      : [11],
                                     # bits 12-15 unused
                                      })
        
        self.num_bits = 16