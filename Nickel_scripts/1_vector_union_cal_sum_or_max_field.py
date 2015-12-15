# ============================================================================
# Name: 1_vector_union_cal_sum_or_max_field.py
# Author:  R. Coghlan, Geoscience Australia
# Date: 2015-10-27
# Desc: This tool unions input polygon vector data using either maximum or sum 
# operations.
#
# Requirements: Tool requires ArcInfo license
# ============================================================================


# Import modules
import arcpy
from arcpy import env

# Overwrite existing outputs
env.overwriteOutput = True

# Script parameters from ArcToolbox GUI
inputvectorslist = arcpy.GetParameter(0)
output = arcpy.GetParameterAsText(1)
function = arcpy.GetParameterAsText(2)
field = arcpy.GetParameterAsText(3)

# Perform union operation
arcpy.AddMessage('Performing union on input data')
arcpy.Union_analysis(inputvectorslist, output)

# loop through fields and add any that start with "field" (as defined
# as a parameter earlier) to a list
fieldlist = [f.name for f in arcpy.ListFields(output) 
                if f.name.startswith(field)]

# depending on the function defined, determine the max or sum value
if function == "MAXIMUM":
    expression = "max([!" + "!, !".join(fieldlist) + "!])"
    newfield = "MAX_" + field
    
if function == "SUM":
    expression = "sum([!" + "!, !".join(fieldlist) + "!])"
    newfield = "SUM_" + field
  
# add new field to populate above value to
arcpy.AddMessage('Adding new field')
arcpy.AddField_management(output, newfield, "DOUBLE")

# Perform the field calculation
arcpy.AddMessage('Calculating {0} field'.format(function))
arcpy.CalculateField_management(output, newfield, expression,
                                "PYTHON_9.3", "#")

arcpy.AddMessage('Processing complete')
