<!-- this markdown file automatically generated. do not edit directly-->

## Landsat 8 Collection 2 Level 2 QA Pixel

**Product Identifer**: `LANDSAT_8_C2_L2_QAPixel`

### Details  
This is the primary QA pixel for Landsat 8 C2L2.   
  
### Flag Descriptions  
  
| Bits  | Flag Name               | Descriptions                                                                                              |  
|-------|-------------------------|-----------------------------------------------------------------------------------------------------------|  
| 0     | Fill                    | 0 - for image data<br>1 - for fill data                                                                   |  
| 1     | Dilated_Cloud           | 0 - for cloud is not dilated or no cloud<br>1 - for cloud dilation                                        |  
| 2     | Cirrus                  | 0 - for Cirrus Confidence: no confidence level<br>set or Low Confidence<br>1 - for high confidence cirrus |  
| 3     | Cloud                   | 0 - for cloud confidence is not high<br>1 - for high confidence cloud                                     |  
| 4     | Cloud_Shadow            | 0 - for Cloud Shadow Confidence is not high<br>1 - for high confidence cloud shadow                       |  
| 5     | Snow                    | 0 - for Snow/Ice Confidence is not high<br>1 - for high confidence snow cover                             |  
| 6     | Clear                   | 0 - if Cloud or Dilated Cloud bits are set<br>1 - if Cloud and Dilated Cloud bits are not set             |  
| 7     | Water                   | 0 - for land or cloud<br>1 - for water                                                                    |  
| 8-9   | Cloud_Confidence        | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |  
| 10-11 | Cloud_Shadow_Confidence | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |  
| 12-13 | Snow_Ice_Confidence     | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |  
| 14-15 | Cirrus_Confidence       | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |  
  
### References docs   
Landsat 8 Collection 2 (C2) Level 2 Science Product (L2SP) Guide (LSDS-1619 Version 2.0, September 2020)  
  
### Confirmed products  
- Google Earth Engine: LANDSAT/LC08/C02/T1_L2  
- EarthExplorer Landsat 8 OLI/TIRS C2 L2  

## Landsat 8 Collection 2 Level 2 QA RADSAT

**Product Identifer**: `LANDSAT_8_C2_L2_QARADSAT`

### Details  
This is the Radiometric Saturation and Terrain Occlusion QA    
  
### Flag Descriptions  
  
| Bits  | Flag Name              | Descriptions                                      |  
|-------|------------------------|---------------------------------------------------|  
| 0     | Band_1_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 1     | Band_2_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 2     | Band_3_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 3     | Band_4_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 4     | Band_5_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 5     | Band_6_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 6     | Band_7_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 7     | Unused                 |                                                   |  
| 8     | Band_9_Data_Saturation | 0 - no saturation<br>1 - saturated data           |  
| 9     | Unused                 |                                                   |  
| 10    | Unused                 |                                                   |  
| 11    | Terrain_Occlusion      | 0 - no terrain occlusion<br>1 - terrain occlusion |  
| 12-15 | Unused                 |                                                   |  
  
  
### References docs   
Landsat 8 Collection 2 (C2) Level 2 Science Product (L2SP) Guide (LSDS-1619 Version 2.0, September 2020)  
  
### Confirmed products  
- Google Earth Engine: LANDSAT/LC08/C02/T1_L2  
- EarthExplorer Landsat 8 OLI/TIRS C2 L2  
    

## Landsat 4-7 Collection 2 Level 2 QA Pixel

**Product Identifer**: `LANDSAT_47_C2_L2_QAPixel`

### Details  
This is the primary QA pixel for Landsat 4-7 Collection 2 Level 2    
  
Note that the three confidence flags have the  value of 1 "reserved" for future  use. The official guide on this (LSDS-1618, see below) says:  
  
> Cloud Shadow, Snow/Ice, and Cirrus Confidence flags in bits 10-15 each have a   
> reserved value for future improvements. They match the respective flags in   
> bits 2, 4, and 5 and may be used interchangeably. [sic]  
  
  
### Flag Descriptions  
  
| Bits  | Flag Name               | Descriptions                                                                                              |  
|-------|-------------------------|-----------------------------------------------------------------------------------------------------------|  
| 0     | Fill                    | 0 - for image data<br>1 - for fill data                                                                   |  
| 1     | Dilated_Cloud           | 0 - for cloud is not dilated or no cloud<br>1 - for cloud dilation                                        |  
| 2     | Unused                  | Unused                                                                                                    |  
| 3     | Cloud                   | 0 - for cloud confidence is not high<br>1 - for high confidence cloud                                     |  
| 4     | Cloud_Shadow            | 0 - for Cloud Shadow Confidence is not high<br>1 - for high confidence cloud shadow                       |  
| 5     | Snow                    | 0 - for Snow/Ice Confidence is not high<br>1 - for high confidence snow cover                             |  
| 6     | Clear                   | 0 - if Cloud or Dilated Cloud bits are set<br>1 - if Cloud and Dilated Cloud bits are not set             |  
| 7     | Water                   | 0 - for land or cloud<br>1 - for water                                                                    |  
| 8-9   | Cloud_Confidence        | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Reserved<br>3 - High confidence              |  
| 10-11 | Cloud_Shadow_Confidence | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Reserved<br>3 - High confidence              |  
| 12-13 | Snow_Ice_Confidence     | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Reserved<br>3 - High confidence              |  
| 14-15 | Unused                  | Unused                                                                                                    |  
  
### References docs   
Landsat 4-7 Collection 2 (C2) Level 2 Science Product (L2SP) Guide (LSDS-1618 Version 3.0 October 2020)  
  
  
### Confirmed products  
- Google Earth Engine: LANDSAT/LE07/C02/T1_L2  
- EarthExplorer Landsat 7 ETM+ C2 L2  
- EarthExplorer Landsat 4-5 TM C2 L2  

## Landsat 4-7 Collection 2 Level 2 Cloud Quality Assessment

**Product Identifer**: `LANDSAT_47_C2_L2_SRCloudQA`

### Details  
The Cloud Quality Assessment QA pixel for Landsat 4-7 Collection 2 Level 2.    
Each of these flags is binary so values of 1 indicate the property is present and a value of 0 indicates the property is absent.  
  
### Flag Descriptions  
  
| Bits  | Flag Name               | Descriptions                 |  
|-------|-------------------------|------------------------------|  
| 0     | DDV                     | Dark Dense Vegetation (DDV)  |  
| 1     | Cloud                   | Cloud                        |  
| 2     | Cloud_Shadow            | Cloud Shadow                 |  
| 3     | Adjacent_to_Cloud       | Adjacent to cloud            |  
| 4     | Snow                    | Snow                         |  
| 5     | Water                   | Water                        |  
| 6-7   | Unused                  | Unused                       |  
  
### References docs   
Landsat 4-7 Collection 2 (C2) Level 2 Science Product (L2SP) Guide (LSDS-1618 Version 3.0 October 2020)  
  
  
### Confirmed products  
- Google Earth Engine: LANDSAT/LE07/C02/T1_L2  
- EarthExplorer Landsat 7 ETM+ C2 L2  
- EarthExplorer Landsat 4-5 TM C2 L2  

## Landsat 4-7 Collection 2 Level 2 QA RADSAT

**Product Identifer**: `LANDSAT_47_C2_L2_QARADSAT`

### Details  
The Radiometric Saturation Quality (QA_RADSAT) band is a bit-packed representation of which sensor bands were saturated during data capture, yielding unusable data.  
  
  
### Flag Descriptions  
  
| Bits  | Flag Name               | Descriptions                                                                                 |  
|-------|-------------------------|----------------------------------------------------------------------------------------------|  
| 0     | Band_1_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 1     | Band_2_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 2     | Band_3_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 3     | Band_4_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 4     | Band_5_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 5     | Band_6_Data_Saturation  | 0 - no saturation<br>1 - saturated data<br>**Band 6 for Landsat 4/5, Band 6L for Landsat 7** |  
| 6     | Band_7_Data_Saturation  | 0 - no saturation<br>1 - saturated data                                                      |  
| 7     | Unused                  | Unused                                                                                       |  
| 8     | Band_6H_Data_Saturation | 0 - no saturation<br>1 - saturated data<br>**Only for Landsat 7, unused for Landsat 4/5**    |  
| 9     | Dropped_Pixel           | 0 - Pixel present<br>1 - detector doesn’t have a value – no data                             |  
| 10-15 | Unused                  |                                                                                              |  
  
  
  
  
### References docs   
Landsat 4-7 Collection 2 (C2) Level 2 Science Product (L2SP) Guide (LSDS-1618 Version 3.0 October 2020)  
  
### Confirmed products  
- Google Earth Engine: LANDSAT/LE07/C02/T1_L2  
- EarthExplorer Landsat 7 ETM+ C2 L2  
- EarthExplorer Landsat 4-5 TM C2 L2  
    

