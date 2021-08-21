---
layout: default
title: MODIS
parent: Product List
---

# MOD13Q1v006_DetailedQA
MODIS/Terra Vegetation Indices 16-Day L3 Global 250m  
    
| Bits  | Flag Name                  | Descriptions                                                                                                                                                                                                                                                                                                      |
|-------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0-1  | VI Quality    | 0 - VI produced with good quality  <br/>1 - VI produced, but check other QA  <br/>2 - Pixel produced, but most probably cloudy  <br/>3 - Pixel not produced due to other reasons than clouds                                                                                                                                  |
| 2-5  | VI Usefulness | 0 - Highest quality <br/>1 - Lower quality  <br/>2 - Decreasing quality  <br/>3 - Decreasing quality  <br/>4 - Decreasing quality  <br/>5 - Decreasing quality  <br/>6 - Decreasing quality  <br/>7 - Lowest quality  <br/>8 - Quality so low that it is not useful  <br/>9 - L1B data faulty  <br/>10 - Not useful for any other reason/not processed   |
| 6-7   | Aerosol Quantity           | 0 - Climatology <br/>1 - Low <br/>2 - Intermediate <br/>3 - High                                                                                                                                                                                                                                                                 |
| 8     | Adjacent cloud detected    | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |
| 9     | Atmosphere BRDF Correction | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |
| 10    | Mixed Clouds               | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |
| 11-13 | Land/Water Mask            | 0 - Shallow ocean <br/>1 - Land (Nothing else but land) <br/>2 - Ocean coastlines and lake shorelines <br/>3 - Shallow inland water <br/>4 - Ephemeral water <br/>5 - Deep inland water <br/>6 - Moderate or continental ocean <br/>7 - Deep ocean                                                                                                   |
| 14    | Possible snow/ice          | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |
| 15    | Possible shadow            | 0 - No <br/>1 - Yes                                                                                                                                                                                                                                                                                                    |



### References docs
- MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.00, June 2015 (Collection 6)  
- [https://lpdaac.usgs.gov/products/mod13q1v006/](https://lpdaac.usgs.gov/products/mod13q1v006/])

    
### Confirmed products:  
- Google Earth Engine: MODIS/006/MOD13Q1  

# MOD13A1v006_DetailedQA
MODIS/Terra Vegetation Indices 16-Day L3 Global 500m  
    
### References docs 
- MODIS Vegetation Index User’s Guide (MOD13 Series) Version 3.00, June 2015 (Collection 6)  
- [https://lpdaac.usgs.gov/products/mod13q1v006/](https://lpdaac.usgs.gov/products/mod13q1v006/)

    
### Confirmed products
- Google Earth Engine: MODIS/006/MOD13A1  