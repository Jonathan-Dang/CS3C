import urllib.request
import urllib.parse
import json


def getUnis(name):
    # Scrape the data.
    url = f"http://universities.hipolabs.com/search?country={name}"

    webData = urllib.request.urlopen(url)
    results = webData.read().decode()
    webData.close()

    # Convert the json result to a dictionary.
    data = json.loads(results)
    return data

def main():
    countryName = input("Display universities from which country?: ")
    uniNames = getUnis(countryName)
    for item in uniNames:
         print(item["name"])


main()
