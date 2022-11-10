## 
# This program prints information about the current weather in a user-chosen city.
#

import urllib.request
import urllib.parse
import json

from Lab8.DataViewToolBox import obtainJSONData, viewJSONData

# Get the location information from the user.
city = input("Enter the location: ")

# Build and encode the URL parameters.
params = {"q": city, "units": "imperial" }
arguments = urllib.parse.urlencode(params)

# Get the weather information.
address = "http://api.openweathermap.org/data/2.5/weather"
appId = "&appid=ae792fa8901c5df470c7f0da29cf46ee"
url = address + "?" + arguments + appId

# Convert the json result to a dictionary.
data = obtainJSONData(url)

# Print the results.
viewJSONData(data)