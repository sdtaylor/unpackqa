from collections import OrderedDict

from .base import Base

# class name should be {product}_{qa band name}
# where product is some unique identifier, ideally for a specific product version.
# and band name is the specific QA band detailed here. Note some products have
# multiple QA bands for different purposes. 
# One class here should define the QA bits for a *single* band for a *single* product. 
class Template(Base):
    """
    # The full product name.
    
    # Detailes about the resulting QA flags, and the mask values. Either in
    # list or table form.
    
    #Specific technical docs and/or website links which the QA info
    #was pulled from
    References doc: LSDS-1328 Version 6.0, September 2020
    
    # The same data product can be distributed via multiple locations. Here list
    # those locations after confirming they match the QA defined in the 
    # reference docs. 
    
    Confirmed products:
        Google Earth Engine: LANDSAT/LC08/C02/T1_L2
        AWS Store XXXXX
    """
    def __init__(self):
    # Two requied things in the init. flag_info details each flag and the bits
    # it encompasses. This is an ordered dictionary so that the order 
    # specified here is fixed, and should start at bit 0. 
    # num_bits is the bit size of the QA band. Most will be 8 or 16. 
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