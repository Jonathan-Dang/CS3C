import urllib.request
import urllib.parse
import json

##
#   obtainJSONData(url)
#       Input: A fully functional JSON url.
#       Output: A dictionary filled with the JSON data set.     | [DICT]
#
def obtainJSONData(url):
    webData = urllib.request.urlopen(url)
    results = webData.read().decode()
    webData.close()
    return json.loads(results)

##
#   viewJSONData(data)
#       Input: Data Dictionary from decoding a JSON data set.
#       Output: Prints out to console the entire JSON data set. | [VOID]
#
def viewJSONData(data):
    for obj in data:
        print(obj)
        print(' '*5, end='')
        if type(data[obj]) is dict:
            for item in data[obj].keys():
                print(f"{item}: {data[obj][item]}")
                print(' '*5, end='')
        elif type(data[obj]) is list:
            for item in data[obj]:
                if type(item) is dict:
                    for key in item.keys():
                        print(' '*5, end='')
                        print(f"{key}: {item[key]}")
                    print("="*75)
                else:
                    print(' '*5, end='')
                    print(f"{item}")
        else:
            print(data[obj])