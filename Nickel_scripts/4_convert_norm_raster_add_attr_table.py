# ============================================================================
# Name: 4_convert_norm_raster_add_attr_table.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: This tool converts the input raster to integer and creates an attribute
# table to accompany it.
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
mutliplier = arcpy.GetParameterAsText(1)
outputFld = arcpy.GetParameterAsText(2)

# Split the list of input rasters into a python list
inputRastersList = inputRasters.split(";")

# process each raster from list
for raster in inputRastersList:
    try: 
        outRasName = os.path.basename(raster) 
        outputRaster = os.path.join(outputFld, outRasName + '_int')
        
        # create raster object for use in processing
        rasObject = Raster(raster)
             
        # multiply input normalised raster by multiplier and then convert to 
        # integer.  Save output
        arcpy.AddMessage("Processing raster {0}".format(outRasName))
        intRaster = Int(rasObject * int(mutliplier))
        intRaster.save(outputRaster)
        
        # Build raster attribute table on output        
        arcpy.AddMessage("\tBuilding table")
        arcpy.BuildRasterAttributeTable_management(outputRaster, "Overwrite")
        
        arcpy.AddMessage("\tOutput Raster: {0}_int".format(outRasName))

    except Exception as e:
        arcpy.AddMessage("Processing failed: {0}".format(outRasName))
        arcpy.AddError(e.message)
        
# Check in any necessary licenses
arcpy.CheckInExtension("spatial")

arcpy.AddMessage('Script complete')
