from collections import OrderedDict

from base import Base

class L8C2L2_QAPixel(Base):
    """
    Landsat 8 Collection 2 Level 2 QA Pixel unpacking.
    
    References doc: LSDS-1328 Version 6.0, September 2020
    
    Confirmed products:
        Google Earth Engine XXXXX
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