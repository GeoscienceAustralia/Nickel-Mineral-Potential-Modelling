# ============================================================================
# Name: 3_normalise_raster.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: This tool normalizes the input raster and saves it in the output folder
#
# Requirements: Tool requires ArcView license & Spatial Analyst extension
# ============================================================================


# Import modules
import arcpy
from arcpy.sa import *
from arcpy import env
import os


# Overwrite existing outputs
env.overwriteOutput = True

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Script parameters from ArcToolbox GUI
inputRasters = arcpy.GetParameterAsText(0)
outputFld = arcpy.GetParameterAsText(1)


# split the list of input rasters into a python list
inputRastersList = inputRasters.split(";")
    
# split the list of input rasters into a python list
inputRastersList = inputRasters.split(";")

for raster in inputRastersList:
    arcpy.AddMessage("Processing {0}".format(raster))
    # setup output names
    outRasName = os.path.basename(str(raster))
    outputRaster = os.path.join(outputFld, outRasName + '_norm')
    arcpy.AddMessage("\tOutput Raster: {0}_norm".format(outRasName))

    # set-up the raster describe object
    descRaster = arcpy.Describe(raster)
    
    # Execute Normalize transformation
    arcpy.AddMessage("\tRunning Normalise Transformation on {0}"
                        .format(outRasName))

    # get values required for normalization function
    maximumRasterValue = arcpy.GetRasterProperties_management(raster, "MAXIMUM")
    minimumRasterValue = arcpy.GetRasterProperties_management(raster, "MINIMUM")
    # create constant rasters
    arcpy.AddMessage('\t\tCreating max constant raster')
    maximumRaster = CreateConstantRaster(maximumRasterValue, "FLOAT",
                                     descRaster.meanCellWidth, descRaster.extent)
    arcpy.AddMessage('\t\tCreating min constant raster')
    minimumRaster = CreateConstantRaster(minimumRasterValue, "FLOAT",
                                     descRaster.meanCellWidth, descRaster.extent)

    try:
        # normalisation formula
        arcpy.AddMessage('\t\tCreating normalised raster')
        normRaster = (raster - minimumRaster)/(maximumRaster - minimumRaster)
        normRaster.save(outputRaster)
        arcpy.AddMessage("\tNormalised raster saved: {0}".format(outputRaster))

    except Exception as e:
        arcpy.AddMessage("Processing failed: {0}".format(outRasName))
        arcpy.AddError(e.message)

# Check in any necessary licenses
arcpy.CheckInExtension("spatial")

arcpy.AddMessage('Processing complete')
