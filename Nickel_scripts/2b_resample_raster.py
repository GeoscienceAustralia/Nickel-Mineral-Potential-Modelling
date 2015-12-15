# ============================================================================
# Name: 2b_resample_raster.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: This tool re-samples the input raster using the snap raster as the
# source for the cellsize. The output raster extent will equal the extent 
# provided by the tool interface.
#
# Requirements: Tool requires ArcView license & Spatial Analyst extension
# ============================================================================


# Import modules
import arcpy
from arcpy.sa import *
from arcpy import env

# Overwrite existing outputs
env.overwriteOutput = True

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Script parameters from ArcToolbox GUI
inputRaster = arcpy.GetParameterAsText(0)
snapRaster = arcpy.GetParameterAsText(1)
outputRaster = arcpy.GetParameterAsText(2)
extents = arcpy.GetParameterAsText(3)

# Set snap raster environment and get snap raster cellsize
env.snapRaster = snapRaster
cellsizex = arcpy.GetRasterProperties_management(snapRaster, "CELLSIZEX")
cellsizey = arcpy.GetRasterProperties_management(snapRaster, "CELLSIZEY")
cellsize = '{0} {1}'.format(str(cellsizex), str(cellsizey))
env.extent = extents

# create temp raster in memory to access
tmpRaster = r"in_memory\tmpRas"

# execute Resample
arcpy.AddMessage("Resampling input raster")
arcpy.Resample_management(inputRaster, tmpRaster, cellsize, "NEAREST")

# Convert null values to zero
arcpy.AddMessage("Converting null values to zero")
outras = Con(IsNull(tmpRaster), 0, tmpRaster)
outras.save(outputRaster)

# delete all from in_memory workspace
arcpy.Delete_management("in_memory")

# Check in any necessary licenses
arcpy.CheckInExtension("spatial")

arcpy.AddMessage('Processing complete')
    