# My project brief

## The question
How have surface urban heat island intensity and land surface temperature patterns changed across the Ibadan metropolitan area over the past decade?

## The data I need
 * Landsat 8/9 Thermal Infrared Sensor (TIRS) satellite imagery series (30m spatial resolution)      https://earthexplorer.usgs.gov
 * Sentinel-2 MSI Level-2A surface reflectance imagery for NDVI calculation https://dataspace.copernicus.eu (10meter bands)
 * GRID3 settlement extent boundaries for Ibadan https://data.grid3.org
 * OpenStreetMap (OSM) administrative boundaries and urban land-use/land-cover classifications https://download.geofabrik.de



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

and:

USGS Landsat EarthExplorer access information

In EarthExplorer, select:

Data Sets → Landsat → Landsat Collection 2 Level-2

Then select:

Landsat 8-9 OLI/TIRS C2 L2

USGS confirms that the Landsat 8/9 Collection 2 Level-2 product contains both Surface Reflectance and Surface Temperature.

6. Set the EarthExplorer search area

I Upload

Ibadan_Metropolitan_AOI.shp

Landsat 8

Use:

LANDSAT/LC08/C02/T1_L2

Landsat 9

Use:

LANDSAT/LC09/C02/T1_L2

Sentinel
MSI
L2A
Cloud cover is less than 10%
Date: Novemebr, 2024 (Dry season for the rural and urban AOI)
Sentinel-2: L0-S2MSI2A
Name: Sentinel-2-L0-S2MSI2A

Description: Product processing from Sentinel-2 S2MSI0 to MSIL2A (S2MSI2A). Sentinel-2 level 0 data is processed to level 2A, which provides atmospherically corrected Surface Reflectance (SR). Additional Level-2A output image products are an Aerosol Optical Thickness (AOT) map, a Water Vapour (WV) map and a Scene Classification (SCL) map.