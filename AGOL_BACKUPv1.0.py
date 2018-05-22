
# coding: utf-8

# # AGOL Backup - Python API 
# 
# 3.29.2018 | Needs error handling, needs logging, notifications
# 
# Richard Merino | richard.merino@raleighnc.gov | merinogeospatial@gmail.com

# In[24]:


# Import Dependencies
import time
import arcgis
from arcgis.gis import GIS
from IPython.display import display
from apscheduler.schedulers.blocking import BlockingScheduler
print ("Import Successful")



# Authenticate AGOL with OAuth2
gis = GIS("https://ral.maps.arcgis.com", client_id='CLIENT_ID_GOES_HERE')
print("Successfully logged in as: " + gis.properties.user.username)



# Global Variables
scheduler = BlockingScheduler()
time_stamp = (time.strftime("%m/%d/%Y") + " >>> " + time.strftime("%H:%M:%S"))




# Create backup function to schedule
def scheduled_backup():
    # Grab all hosted feature layers
    my_featurelayers = gis.content.search(query="owner:richard.merino@raleighnc.gov_ral", item_type="Feature Layer")

    # Convert all hosted feature layers to choice of format, in my case GeoJson
    for i in my_featurelayers:
        i.export(i.title, 'GeoJson', parameters=None, wait=True)
        print (time_stamp + " | %s has sucessfully exported" % (i.title))

    # Grab all newly created GeoJson
    my_geojsons = gis.content.search(query="owner:richard.merino@raleighnc.gov_ral", item_type="GEOJson")
    for i in my_geojsons:
        i.download(save_path='C:\\Users\\merinor\\Documents\\Data')
    print (time_stamp + " | Items saved in specified location")

    delete_items(my_geojsons)
    print (time_stamp + " | Temporary exports have been deleted")

    #!#!#! Generate log locally or place in AGOL, append to log each iteration #!#!#!
    
    return "Back up completed on" + time_stamp
    
# Starts schedule session
scheduler.add_job(scheduled_backup, 'interval', hours=12)
scheduler.start()


