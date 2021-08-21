---
layout: default
title: Landsat
parent: Product List
has_toc: true
---

# L8C2L2_QAPixel

Landsat 8 Collection 2 Level 2 QA Pixel unpacking.

| Bits  | Flag Name               | Descriptions                                                                                              |
|-------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| 0     | Fill                    | 0 - for image data<br>1 - for fill data                                                                   |
| 1     | Dilated Cloud           | 0 - for cloud is not dilated or no cloud<br>1 - for cloud dilation                                        |
| 2     | Cirrus                  | 0 - for Cirrus Confidence: no confidence level<br>set or Low Confidence<br>1 - for high confidence cirrus |
| 3     | Cloud                   | 0 - for cloud confidence is not high<br>1 - for high confidence cloud                                     |
| 4     | Cloud Shadow            | 0 - for Cloud Shadow Confidence is not high<br>1 - for high confidence cloud shadow                       |
| 5     | Snow                    | 0 - for Snow/Ice Confidence is not high<br>1 - for high confidence snow cover                             |
| 6     | Clear                   | 0 - if Cloud or Dilated Cloud bits are set<br>1 - if Cloud and Dilated Cloud bits are not set             |
| 7     | Water                   | 0 - for land or cloud<br>1 - for water                                                                    |
| 8-9   | Cloud Confidence        | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |
| 10-11 | Cloud Shadow Confidence | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |
| 12-13 | Snow/Ice Confidence     | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |
| 14-15 | Cirrus Confidence       | 0 - for no confidence level set<br>1 - Low confidence<br>2 - Medium confidence<br>3 - High confidence     |
    
### References docs 
- LSDS-1328 Version 6.0, September 2020
    
### Confirmed products
- Google Earth Engine: LANDSAT/LC08/C02/T1_L2

# L8C2L2_QARADSAT

Landsat 8 Collection 2 Level 2 QA RADSAT unpacking.
aka. Radiometric Saturation and Terrain Occlusion QA
    
| Bits  | Flag Name              | Descriptions                                      |
|-------|------------------------|---------------------------------------------------|
| 0     | Band 1 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 1     | Band 2 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 2     | Band 3 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 3     | Band 4 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 4     | Band 5 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 5     | Band 6 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 6     | Band 7 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 7     | Unused                 |                                                   |
| 8     | Band 9 Data Saturation | 0 - no saturation<br>1 - saturated data           |
| 9     | Unused                 |                                                   |
| 10    | Unused                 |                                                   |
| 11    | Terrain occlusion      | 0 - no terrain occlusion<br>1 - terrain occlusion |
| 12-15 | Unused                 |                                                   |

### References docs 
- LSDS-1328 Version 6.0, September 2020
    
### Confirmed products
- Google Earth Engine: LANDSAT/LC08/C02/T1_L2
