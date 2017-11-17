#Credits - Tim Hohn modified script from original source below
#Exports all map documents in a specific directory
#Base script taken from here and modified:  http://support.esri.com/en/technical-article/000012420

#Import modules here
import arcpy, os

print ('Hello, finding workspace now...')

#Set workspace location here
arcpy.env.workspace = ws = r"C:\Test"

print ('Finding .mxd files now...')

#Create list of .mxd files within the workspace.  In this case the asterisk (*) will search for all .mxds existing within the specified workspace. 
mxd_list = arcpy.ListFiles("*.mxd")

print ('Exporting to PDF now...')

for mxd in mxd_list:
    
    current_mxd = arcpy.mapping.MapDocument(os.path.join(ws, mxd))
    pdf_name = mxd[:-4] + ".pdf"
    arcpy.mapping.ExportToPDF(current_mxd, pdf_name)
 
print ('Complete, thank you for using Map Exporter!')
