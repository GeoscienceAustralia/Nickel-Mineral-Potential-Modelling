# ============================================================================
# Name: 5_populate_table.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: Populates the input raster attribute table with Importance, 
# Applicability and Confidence fields.  Using these fields a total weight 
# field is calculated (optional).
#
# Requirements: Tool requires ArcView 10.1 & Spatial Analyst extension
# ============================================================================


# Import modules
import arcpy
from arcpy import env

# Overwrite existing outputs
env.overwriteOutput = True

# Script parameters from ArcToolbox GUI
inputRaster = arcpy.GetParameterAsText(0)
Importance = arcpy.GetParameterAsText(1)
Applicability = arcpy.GetParameterAsText(2)
Confidence = arcpy.GetParameterAsText(3)
Weight = arcpy.GetParameterAsText(4)

# build attribute table
arcpy.BuildRasterAttributeTable_management(inputRaster, "Overwrite")

# add fields to table
arcpy.AddMessage("Adding Importance field")
arcpy.AddField_management(inputRaster, "Importance", "FLOAT", "", "", "", "",
                          "NULLABLE", "REQUIRED")
arcpy.AddMessage("Adding Applicability field")
arcpy.AddField_management(inputRaster, "Applicability", "FLOAT", "", "", "", 
                          "", "NULLABLE", "REQUIRED")
arcpy.AddMessage("Adding Confidence field")
arcpy.AddField_management(inputRaster, "Confidence", "FLOAT", "", "", "", "", 
                          "NULLABLE", "REQUIRED")

# loop through each row in table and update fields to user defined
# values.  If the row value = 0 then populate fields with 0.
arcpy.AddMessage("Updating values")

fields = ['Value', 'Importance', 'Applicability', 'Confidence'] 
     
with arcpy.da.UpdateCursor(inputRaster, fields) as cursor:
    for row in cursor:
        if not row[0] == 0:
            row[1] = Importance
            row[2] = Applicability
            row[3] = Confidence
        else:
            row[1] = 0
            row[2] = 0
            row[3] = 0
        cursor.updateRow(row)

# if the weight option was ticked, create field and then
# calculate weight
if Weight == "true":
    arcpy.AddMessage("Adding Weight field")
    arcpy.AddField_management(inputRaster,"Weight" , "FLOAT", "", "", "", "", 
                              "NULLABLE", "REQUIRED")
    arcpy.AddMessage("Calculating Weight")
    arcpy.CalculateField_management(inputRaster, "Weight",
                                    "!Importance! * !Applicability! * "
                                    "!Confidence!", "PYTHON", "#")

arcpy.AddMessage('Processing complete')
