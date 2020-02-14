#!/usr/bin/env python3
import json
import os
import time


jsonFile = open("TFi_Tx_configuration.json", "r") # Open the JSON file for reading
data = json.load(jsonFile) # Read the JSON into the buffer
jsonFile.close() # Close the JSON file

dict = {
    "Stream_to_Server" : "",
    "ID" : "",
    "MAC" : "",
    "Portion_of_Time" : "",
    "Best_Phase_Shift" : ""
}

#print(dict)

data['Sensors_Attribute'].append(dict)

print(data)


# save changing
jsonFile = open("TFi_Tx_configuration.json", "w+")
jsonFile.write(json.dumps(data, sort_keys=True, indent=4))
jsonFile.close()


#print(data['Sensors_Attribute'][0])

#print(type(data["Sensors_Attribute"][0]))