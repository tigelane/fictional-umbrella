# importing the requests library
import requests

# api-endpoint
URL = "http://intersight.com//api/v1/virtualization/VmwareVirtualMachines"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

for a in data["Results"]:
    print (a["name"])

