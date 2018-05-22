
# coding: utf-8

# Important Code Blocks for working with the Python API
# 
# Richard Merino | merinogeospatial@gmail.com | richard.merino@raleighnc.gov
# 

# Content Manager reference material - https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.gis.toc.html#contentmanager
# 
# The blocks below can be use as building blocks to create scripts for creating automated processes. This notebook contains necessary blocks for extracting and backing up your feature layers. Can be written in time loop after authentication for persistently running script. Note that federated logins must use this authentication framework for now, username and password authentication not working for our type of login
# 
# For updating feature layers, refer to - https://developers.arcgis.com/python/guide/editing-features/


# IMPORT DEPENDENCIES
import arcgis
from arcgis.gis import GIS
from IPython.display import display
print ("Import Successful")

# AUTHENTICATE WITH OAUTH2
gis = GIS("https://ral.maps.arcgis.com", client_id='PUT_CLIENT_ID_HERE')
print("Successfully logged in as: " + gis.properties.user.username)

type(gis.content) # check content manager, unnecessary


# CREATE CONTENT QUERY, RETURNS LIST OF OBJECTS
search_result = gis.content.search(query="owner:richard.merino@raleighnc.gov_ral", item_type="Feature Layer")
search_result


# DISPLAYS SEARCH RESULTS 
from IPython.display import display
for item in search_result:
    display(item)


# GET ITEM ID
tree_data = search_result[1]
tree_data_id = tree_data.id
print(tree_data_id)


"""# PUTTING ALL IDs FROM QUERY INTO LIST
item_id_list = []
for i in search_result:
    item_id_list.append(gis.content.get(str(i.id)))
print(item_id_list)"""


# GETTING ID IS UNNCESSARY - PULL STRAIGHT FROM OBJECT LIST
for i in search_result:
    i.download(save_path='C:\\Users\\merinor\\Documents\\Data')
print ("Items saved in specified location")
    


# SET VARIABLE TO ACCESS SPECIFIED ITEM
get_item = gis.content.get('207450656b6641618994413617fdcbb5')
get_item

# RETURNS JSON FORMAT METADATA - NO SPATIAL DATA INCLUDED, DO NOT USE TO BACKUP
data = get_item.get_data()
data


# WRITE METADATA TO JSON
import json
with open('data.json', 'w') as file:
  json.dump(data, file, ensure_ascii=False)
print ("JSON Backup created in location of this notebook") 
# Does not contain spatial data > find way to export geojson



# DOWNLOADS ITEM TO PATH (DOES NOT CHANGE FORMAT)
get_item.download(save_path='C:\\Users\\Richard\\Desktop\\DATA')
print ("Item saved in specified location")


#EXPORTS SPECIFIED ITEM TO SPECIFIED FORMAT - WILL SAVE IN YOUR AGOL CONTENTS LOCATION
get_item.export('Tree_subset(TEST)', 'GeoJson', parameters=None, wait=True)


search_result2 = gis.content.search(query="owner:richard.merino@raleighnc.gov_ral", item_type="GeoJSON")
search_result2

# INTERATION OVER DICTIONARIES - .item creates dictionary as tuple to be unpacked
for key,value in dictionary.items():
    print(key, 'corresponds to', value)
 
    
