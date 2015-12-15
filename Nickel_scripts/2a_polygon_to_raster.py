# ============================================================================
# Name: 2a_polygon_to_raster.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: This tool converts input polygon vector files to raster. The output 
# raster extent will equal the extent provided by the tool interface.
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
inputpolygon = arcpy.GetParameterAsText(0)
field = arcpy.GetParameterAsText(1)
outputraster = arcpy.GetParameterAsText(2)
snapraster = arcpy.GetParameterAsText(3)
cellassign = arcpy.GetParameterAsText(4)
extents = arcpy.GetParameterAsText(5)

# setup extents to snap rasters to
env.snapRaster = snapraster
env.extent = extents
cellsize = snapraster
arcpy.env.outputCoordinateSystem = snapraster

# create temp raster in memory to access
tmpraster = r"in_memory\tmpRas"

# Convert polygon to raster
arcpy.AddMessage("Converting input layer to raster")
arcpy.PolygonToRaster_conversion(inputpolygon, field, tmpraster,
                                 cellassign, "", cellsize)

arcpy.AddMessage("Converting null values to zero")
outras = Con(IsNull(tmpraster), 0, tmpraster)
outras.save(outputraster)

# delete all from in_memory workspace
arcpy.Delete_management("in_memory")

# Check in any necessary licenses
arcpy.CheckInExtension("spatial")

arcpy.AddMessage('Processing complete')
