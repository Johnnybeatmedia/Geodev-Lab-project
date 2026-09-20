Data Preparation and Quality checks 
The downloaded files are in EPSG: 4326 and re-projected into EPSG: 32631 - WGS 84 / UTM Zone 31N.
This enables clipping and area square calculation for the study area.
Reprojected and Clipping: Settlement extent from grid 3, LST for Nov2024, Ibadan study area.
Five Quality Checks:
1. CRS: All layers use EPSG: 32631
2. Geometry: Checked for duplicate features and null values
3. Duplicate: Checked for duplicate features
4. Attributes: Checked for missing/incomplete values
5. Location: Checked features against Ibadan metropolis
Problems/Actions: CRS differences were corrected by reprojections and other issues were checked and flagged where necessary.
Analysis-ready file: Saved as a GeoPackage (".gpkg") in the project repository
