<!-- this markdown file automatically generated. do not edit directly-->

## MODIS Vegetation Indices (MOD13) Collection 6

**Product Identifer**: `MOD13_V6_DetailedQA`

### Details  
The MODIS Vegatation indice (VI) QA band. This specification is valid for most of the MOD13 products, with the exception of MOD13C1 and MOD13C2.  
  
MOD13 Collection 6.1 is identical to Collection 6.0.  
  
While the flag specifications are the same for the following 4 products, the details are slightly different for each within the `VI_Usefulness` flag. See the product guide for details.  
  
- MOD13Q1 - 16-day 250m VI  
- MOD13A1 - 16-day 500m VI  
- MOD13A2 - 16-day 1km VI  
- MOD13A3 - Monthly 1km VI  
  
  
### Flag Descriptions  
  
| Bits  | Flag Name                  | Descriptions                                                                                                                                                                                                                                                                                                      |  
|-------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 0-1   | VI_Quality     | 0 - VI produced with good quality  <br/>1 - VI produced, but check other QA  <br/>2 - Pixel produced, but most probably cloudy  <br/>3 - Pixel not produced due to other reasons than clouds                                                                                                                                  |  
| 2-5   | VI_Usefulness  | 0 - Highest quality <br/>1 - Lower quality  <br/>2 - Decreasing quality  <br/>3 - Decreasing quality  <br/>4 - Decreasing quality  <br/>5 - Decreasing quality  <br/>6 - Decreasing quality  <br/>7 - Lowest quality  <br/>8 - Quality so low that it is not useful  <br/>9 - L1B data faulty  <br/>10 - Not useful for any other reason/not processed   |  
| 6-7   | Aerosol_Quantity           | 0 - Climatology <br/>1 - Low <br/>2 - Intermediate <br/>3 - High                                                                                                                                                                                                                                                                 |  
| 8     | Adjacent_cloud_detected    | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |  
| 9     | Atmosphere_BRDF_Correction | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |  
| 10    | Mixed_Clouds               | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |  
| 11-13 | Land_Water_Mask            | 0 - Shallow ocean <br/>1 - Land (Nothing else but land) <br/>2 - Ocean coastlines and lake shorelines <br/>3 - Shallow inland water <br/>4 - Ephemeral water <br/>5 - Deep inland water <br/>6 - Moderate or continental ocean <br/>7 - Deep ocean                                                                                                   |  
| 14    | Possible_snow_ice          | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |  
| 15    | Possible_shadow            | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |  
  
  
### References docs   
MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.00, June 2015 (Collection 6)    
MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.10, Sept 2019 (Collection 6.1)    
  
### Confirmed products  
- [https://lpdaac.usgs.gov/products/mod13q1v006/](https://lpdaac.usgs.gov/products/mod13q1v006/)  
- [https://lpdaac.usgs.gov/products/mod13q1v061/](https://lpdaac.usgs.gov/products/mod13q1v061/)  
  
- [https://lpdaac.usgs.gov/products/mod13a1v006/](https://lpdaac.usgs.gov/products/mod13a1v006/)  
- [https://lpdaac.usgs.gov/products/mod13a1v061/](https://lpdaac.usgs.gov/products/mod13a1v061/)  
  
- [https://lpdaac.usgs.gov/products/mod13a2v006/](https://lpdaac.usgs.gov/products/mod13a2v006/)  
- [https://lpdaac.usgs.gov/products/mod13a2v061/](https://lpdaac.usgs.gov/products/mod13a2v061/)  
  
- [https://lpdaac.usgs.gov/products/mod13a3v006/](https://lpdaac.usgs.gov/products/mod13a3v006/)  
- [https://lpdaac.usgs.gov/products/mod13a3v061/](https://lpdaac.usgs.gov/products/mod13a3v061/)  
  
- Google Earth Engine: MODIS/006/MOD13Q1    
- Google Earth Engine: MODIS/006/MOD13A1    
- Google Earth Engine: MODIS/006/MOD13A2    

## MODIS Vegetation Indices CMG (MOD13) Collection 6

**Product Identifer**: `MOD13C_V6_DetailedQA`

### Details  
The MODIS Vegatation indice (VI) QA band for the CMG (climate modeling grid) products.  
  
This specification is identical to the other MOD13 products except that a `Geospatial_quality` flag is added, and the `Possible_snow_ice` and `Possible_shadow` flags removed.  
  
MOD13 Collection 6.1 is identical to Collection 6.0.  
          
- MOD13C1 - 16-day 0.05-deg VI  
- MOD13C2 - monthly 0.05-deg VI  
  
### Flag Descriptions  
  
| Bits  | Flag Name                  | Descriptions                                                                                                                                                                                                                                                                                                          |  
|-------|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 0-1   | VI_Quality     | 0 - VI produced with good quality  <br/>1 - VI produced, but check other QA  <br/>2 - Pixel produced, but most probably cloudy  <br/>3 - Pixel not produced due to other reasons than clouds                                                                                                                                      |  
| 2-5   | VI_Usefulness  | 0 - Highest quality <br/>1 - Lower quality  <br/>2 - Decreasing quality  <br/>3 - Decreasing quality  <br/>4 - Decreasing quality  <br/>5 - Decreasing quality  <br/>6 - Decreasing quality  <br/>7 - Lowest quality  <br/>8 - Quality so low that it is not useful  <br/>9 - L1B data faulty  <br/>10 - Not useful for any other reason/not processed   |  
| 6-7   | Aerosol_Quantity           | 0 - Climatology <br/>1 - Low <br/>2 - Intermediate <br/>3 - High                                                                                                                                                                                                                                                      |  
| 8     | Adjacent_cloud_detected    | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                   |  
| 9     | Atmosphere_BRDF_Correction | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                   |  
| 10    | Mixed_Clouds               | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                   |  
| 11-13 | Land_Water_Mask            | 0 - Shallow ocean <br/>1 - Land (Nothing else but land) <br/>2 - Ocean coastlines and lake shorelines <br/>3 - Shallow inland water <br/>4 - Ephemeral water <br/>5 - Deep inland water <br/>6 - Moderate or continental ocean <br/>7 - Deep ocean                                                                    |  
| 14-15 | Geospatial_quality         |  0 - ≤ 25% of the finer 1-km resolution contributed to this CMG pixel<br>1 - > 25% and ≤ 50% of the finer 1-km resolution contributed to this CMG pixel<br>2 - > 50% and ≤ 75% of the finer 1-km resolution contributed to this CMG pixel<br>3 - > 75% of the finer 1-km resolution contributed to this CMG pixel     |  
  
### References docs   
MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.00, June 2015 (Collection 6)    
MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.10, Sept 2019 (Collection 6.1)    
  
### Confirmed products  
- [https://lpdaac.usgs.gov/products/mod13c1v006/](https://lpdaac.usgs.gov/products/mod13c1v006/)  
- [https://lpdaac.usgs.gov/products/mod13c1v061/](https://lpdaac.usgs.gov/products/mod13c1v061/)  
  
- [https://lpdaac.usgs.gov/products/mod13c2v006/](https://lpdaac.usgs.gov/products/mod13c2v006/)  
- [https://lpdaac.usgs.gov/products/mod13c2v061/](https://lpdaac.usgs.gov/products/mod13c2v061/)  

## MODIS Collection 6 LAI/FPAR Products FparLAI_QC

**Product Identifer**: `MODIS_LAIV6_FparLAI_QC`

### Details  
The MODIS Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR).   
  
This and `MODIS_LAIV6_FparExtra_QC` both compliment each other.    
  
There are several MODIS LAI/FPAR products which all use the same algorithms and resulting QA info.  
  
- MOD15A2H - Terra/500m/8day  
- MYD15A2H - Aqua/500m/8day  
- MCD15A2H - Terra+Aqua/500m/8day  
- MCD15A3H - Terra+Aqua/500m/4day  
  
Two recent versions, v006 and v0061, also have identical QA info for all 4 products.  
  
### Flag Descriptions  
  
| Bits  | Flag Name       | Descriptions                |  
|-------|-----------------|------------------------------|  
| 0     | MODLAND_QC      | 0 - Good quality (main algorithm with or without saturation)<br>1 - Other quality (back−up algorithm fill values) |  
| 1     | Sensor          | 0 - Terra<br>1 - Aqua |  
| 2     | Dead_Detector   | 0 - Detectors apparently fine for up to 50% of channels 1, 2<br>1 - Dead detectors caused >50% adjacent detector retrieval    |  
| 3-4   | Cloud_State     | 0 - Significant clouds NOT present (clear)<br>1 - Significant clouds WERE present<br>2 - Mixed cloud present in pixel<br>3 - Cloud state not defined, assumed clear  |  
| 5-7   | SCF_QC          | Five−level confidence score<br>0 - Main (RT) method used with no saturation, best result possible<br>1 - Main (RT) method used with saturation, good and very usable<br> 2 - Main (RT) method failed due to bad geometry, empirical algorithm used<br>3 - Main (RT) method failed due to problems other than geometry, empirical algorithm used<br>4 - Pixel not produced at all, value couldn't be retrieved (possible reasons: bad L1B data, unusable MOD09GA data)<br>|  
  
### References docs   
MODIS Collection 6 (C6) LAI/FPAR Product User’s Guide (April 21, 2020)  
MODIS Collection 6.1 (C6.1) LAI/FPAR Product User’s Guide (April 21, 2021)  
  
### Confirmed products  
- Google Earth Engine: MODIS/006/MCD15A3H  
- EarthExplorer MCD15A2H V6   
- EarthExplorer MCD15A3H V6   
- EarthExplorer MOD15A2H V6   
- EarthExplorer MYD15A2H V6   

## MODIS Collection 6 LAI/FPAR Products FparExtra_QC

**Product Identifer**: `MODIS_LaiFparV6_FparExtra_QC`

### Details  
The MODIS Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR).   
  
This and `MODIS_LAIV6_FparLAI_QC` both compliment each other.    
  
There are several MODIS LAI/FPAR products which all use the same algorithms and resulting QA/QC info.  
  
- MOD15A2H - Terra/500m/8day  
- MYD15A2H - Aqua/500m/8day  
- MCD15A2H - Terra+Aqua/500m/8day  
- MCD15A3H - Terra+Aqua/500m/4day  
  
Two recent versions, v006 and v0061, also have identical QA info for all 4 products.  
  
### Flag Descriptions  
  
| Bits | Flag Name          | Description                                                                                      |  
|------|--------------------|--------------------------------------------------------------------------------------------------|  
| 0-1  | LandSea            | 0 - LAND<br>1 - SHORE<br>2 - FRESHWATER<br>3 - OCEAN                                             |  
| 2    | Snow_Ice           | 0 - No snow/ice detected<br>1 - Snow/ice deteced                                                 |  
| 3    | Aerosol            | 0 - No or low atmospheric aerosol levels detected<br>1 - Average or high aerosol levels detected |  
| 4    | Cirrus             | 0 - No cirrus detected<br>1 - Cirrus was detected                                                |  
| 5    | Internal_CloudMask | 0 - No clouds<br>1 - Clouds were detected                                                        |  
| 6    | Cloud_Shadow       | 0 - No cloud shadow detected<br>1 - Cloud shadow detected                                        |  
| 7    | SCF_Biome_Mask     | 0 - Biome outside interval<br>1 - Biome in interval                                              |  
      
### References docs   
MODIS Collection 6 (C6) LAI/FPAR Product User’s Guide (April 21, 2020)  
MODIS Collection 6.1 (C6.1) LAI/FPAR Product User’s Guide (April 21, 2021)  
  
### Confirmed products  
- Google Earth Engine: MODIS/006/MCD15A3H  
- EarthExplorer MCD15A2H V6   
- EarthExplorer MCD15A3H V6   
- EarthExplorer MOD15A2H V6   
- EarthExplorer MYD15A2H V6   

