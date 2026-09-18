# My project brief

## The question
How have surface urban heat island intensity and land surface temperature patterns changed across the Ibadan metropolitan area over the past decade?

## The data I need
Where it came from with source link: 
* Landsat 8/9 Surface Reflectance (Band 2) (30m spatial resolution)    
Source:  https://earthexplorer.usgs.gov

Source link:
 * Sentinel-2 MSI Level-2A surface reflectance imagery for NDVI calculation https://dataspace.copernicus.eu (10meter bands) https://browser.dataspace.copernicus.eu/?zoom=9&lat=7.64296&lng=4.40488&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX18ckAp0Arg0Gk2liK5tWA3RUNTksNdUImd3MTEkxxF9MEi%2BTP6L%2BrpO0VvnrcPpS5jac4vGv97UFGLlWkwfm65ctyU5LkGEebqMZIuSzTD3EGtlqaY7qQ96&datasetId=S2_L2A_CDAS&fromTime=2025-01-14T00%3A00%3A00.000Z&toTime=2025-01-14T23%3A59%3A59.999Z&layerId=SCENE-CLASSIFICATION

Dataset Name: LC08_L2SP_191055_20260120_20260129_02_T1_SR_B2
Geometry/ Data Type: Raster (Grid)
Dimensions/ Features Count: 7,581
Columns x7,741 rows (1 band)
Pixel Resolution: 30m x 30m
Coordinate Reference System (CRS): EPSG:32631 - WGS 84 / UTM zone 31N (Projected Coordinate System)

Key Properties / Attributes:
Units: meters
Celestial Body: Earth
Pixel Values: Surface Reflectance (Blue Band)
Data Quality &Gaps: Black background/border areas outside the scene footprint contain NoData (null) values. The data has an ensemble accuracy within 2 meters

https://browser.dataspace.copernicus.eu/?zoom=9&lat=7.6443&lng=3.49915&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX1%2BLodm10k1XEgTxMhOg7mylhfNEdhYnHAdmlGs9%2FOAi0WykZVRw06Zuo7C2IIqGTXV7I9fOuq0tswbwZU2CQGJq8qnwKQkCYhiKY%2BYdvW4gucHClPBSo7DP&datasetId=S2_L2A_CDAS&fromTime=2025-01-14T00%3A00%3A00.000Z&toTime=2025-01-14T23%3A59%3A59.999Z&layerId=SCENE-CLASSIFICATION

Dataset 2
OpenStreetMap Vector Layer (QuickOSM)

 * GRID3 settlement extent boundaries for Ibadan https://data.grid3.org

https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about

 * OpenStreetMap (OSM) administrative boundaries and urban land-use/land-cover classifications https://download.geofabrik.de

https://www.openstreetmap.org/search?query=ibadan%2C+nigeria&zoom=6&minlon=-5.383300781250001&minlat=3.337953961416485&maxlon=22.741699218750004&maxlat=14.817370620155266#map=11/7.3784/3.8972

AOI: Ibadan Metropolises with 6 features and 9 columns ( fid, ID_0, ISO, NAME_0, ID_0, NAME_1, ID_2, NAME_2, TYPE_2,)
Geometry type: Vector


Summary
The GRID3 NGA - Settlement Extents v4.1 dataset consists of a geographic representation of settlements in Nigeria. Settlement extents are further delineated into settlement blocks nested within urban and small settlement areas, generated from integrated road, railway, river, building footprints, and remote-sensing inputs. Each block is enriched with morphological, environmental, and building metrics.

This version supersedes the GRID3 NGA - Settlement Extents v4.0. The following changes were made:

Revision of block delineation methodology resulting in new block geometries.
Removal of hamlets and edge-blocks with zero-building count
Addition of airports to the block classifications and removal of es_class (extent size) from the attributes and classification.
For more information on the methodology and data sources used during the production of these data, click here.

Dataset citation

Center for Integrated Earth System Information (CIESIN), Columbia University. 2026. GRID3 NGA - Settlement Extents v4.1. New York: Columbia University. https://doi.org/10.7916/73v5-mq06. Accessed [DAY MONTH YEAR].


USGS Landsat Collection 2 Level-2 documentation

The EarthExplorer search area

I Upload

Ibadan_Metropolitan_AOI.shp

Landsat 8

LANDSAT/LC08/C02/T1_L2

LANDSAT/LC09/C02/T1_L2

Sentinel
MSI
L2A
Cloud cover is less than 10%
Date: November, 2024 (Dry season for the rural and urban AOI)
Sentinel-2: L0-S2MSI2A
Name: Sentinel-2-L0-S2MSI2A

Description: Product processing from Sentinel-2 S2MSI0 to MSIL2A (S2MSI2A). Sentinel-2 level 0 data is processed to level 2A, which provides atmospherically corrected Surface Reflectance (SR). Additional Level-2A output image products are an Aerosol Optical Thickness (AOT) map, a Water Vapour (WV) map and a Scene Classification (SCL) map.
