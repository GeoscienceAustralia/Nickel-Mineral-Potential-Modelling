# Nickel-Mineral-Potential-Modelling

----------

A collection of ESRI ArcGIS tools to perform GIS-based mineral (Nickel) prospectivity analysis using a knowledge-driven approach to combine different datasets in the study of ***Potential for intrusion-hosted Ni-Cu-PGE sulfide deposits in Australia: A continental-scale analysis of mineral system prospectivity.***

###**Metadata**###


- http://www.ga.gov.au/metadata-gateway/metadata/record/83884

###**Dependancies**###


- ESRI ArcGIS 10.2 (ArcInfo Licence)
- ESRI ArcGIS Spatial Analysis Extension
- Python 2.7

###**Configuration**###

Download package, unzip and add **GA\_Nickel\_Toolbox\_2015.tbx** to your ArcGIS toolbox


## **Project Description** ##

This study of Australia’s potential for tholeiitic intrusion-hosted Ni-Cu-PGE sulfide deposits utilises a mineral systems approach as the basis for a knowledge-driven GIS-based prospectivity analysis. The conceptual model for the formation of tholeiitic intrusion-hosted Ni-Cu-PGE sulfide deposits incorporates four mineral system components: (1) energy sources or drivers of the ore-forming system; (2) crustal and mantle lithospheric architecture; (3) sources of ore constituents (i.e., Ni, PGE, Cu, S in magmatic systems); and (4) gradients in ore depositional physico-chemical parameters. For each of the four system components 'theoretical’ conceptual criteria were developed which represent geological processes essential for the formation of a major ore deposit. These processes are represented by `mappable criteria’ which are themselves represented by individual geoscientific datasets. The GIS analysis of prospectivity uses a wide range of continental- to regional-scale geological, geophysical and geochemical datasets, each weighted with fuzzy logic values between 0 and 1 according to expert opinion. Summed values for each of the four mineral system components contributes a maximum of 25% of the final assessment of mineral potential, reflecting the need for all four mineral system components to have been present to form a major ore deposit.


## **Toolbox Description** ##

The following tools are available through the toolbox.  Please refer to the publication listed below for detailed workflow and data processing descriptions.


#####1. Union input data + calculate sum or max
Merges vector data into a single vector layer using the union process and takes either the sum or maximum of the input layers to form the new value.

#####2a. Polygon To Raster
Polygon to raster tool to convert vector files to raster.

#####2b. Resample raster to source raster
Alters the input raster dataset by changing the cell size and origin to match the snap raster using the nearest neighbour resampling algorithm.

#####3. Normalize Raster
Creates normalized (0-1) raster for each input file.

#####4. Convert to Integer and create attribute table
Converts raster to integer using the supplied multiplier and adds an attribute table to the output raster.

#####5. Populate I, A, C and W fields
Populates the raster attribute table with Importance, Applicability and Confidence fields and values. Using these fields a total weight field is calculated.

#####6a. Weighted sum - use feature weight
Executes a weighted sum calculation using the weight values stored in the attribute table of each input raster

#####6b. Weighted sum - use equal weight
Executes a weighted sum calculation using an equal weight given to each input raster. 





## Publications ##

Dulfer, H., Skirrow R.G., Champion, D.C., Highet, L.M., Czarnota, K., Coghlan, R., P. Milligan., P., 2015. Potential for intrusion-hosted Ni-Cu-PGE sulfide deposits in Australia: A continental-scale analysis of mineral system prospectivity. Record 2015/xx. Geoscience Australia, Canberra. http://dx.doi.org/10.11636/Record.2015.xxx
