Data Preparation and Quality checks 
The downloaded files are in EPSG: 4326 and re-projected into EPSG: 32631 - WGS 84 / UTM Zone 31N.
This enables clipping and area square calculation for the study area. For example, Ibadan North is 26.33sqkm, Ib SW is 40 sq km
Reprojected and Clipping: Settlement extent from grid 3, LST for Nov2024, LST for Jan2026.
Five Quality Checks:
1. CRS: All layers use EPSG: 32631
2. Geometry: Checked for duplicate features and null values. The study_area total features 2,546,560
3. Duplicates: Checked for duplicate features and filtered to 47032
4. Attributes: Checked for missing/incomplete values. 
LST for Nov2024
Dimensions: X: 7581 Y: 7741 Bands: 1
Origin: 429585.0000000000000000,915015.0000000000000000
Pixel Size: 30,-30
Band count: 1
Number Band
NoData: 0
Min: 172.0000000000
Max:57159.0000000000

LST for Jan 2026
Dimensions: X: 7581 Y: 7741 Bands: 1
Origin: 29585.0000000000000000,915015.0000000000000000
Pixel Size:30,-30
Band count: 1
Number: 1
NoData: 0
Min: 95.0000000000
Max: 57473.0000000000

5. Location: Checked features against Ibadan metropolis. Setllement_extent and AOI
Problems/Actions: CRS differences were corrected by reprojections; other issues were flagged where necessary.
Analysis-ready file: Saved as a GeoPackage (".gpkg") in the project repository.



