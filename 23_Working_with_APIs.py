import requests
import json
import pprint

# https://www.youtube.com/watch?v=9N6a-VLBa2I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=47


couriers_file = 'C:/Dev/aftership/files/couriers5.json'

### aftership API
url = "https://api.aftership.com/v4/couriers"

headers = {
    "Content-Type": "application/json",
    "as-api-key": "asat_3ea205e3046548c2941c3bf977479a3a",
    "timeout": "10"
}
###

response = requests.request("GET", url, headers=headers)
#print(response.text)
response.encoding = 'utf-8'
resp_dict = json.loads(response.text) # loads is used to load a Json string into a Python dictionary
list_of_couriers = resp_dict['data']['couriers']

#OR#
list_of_couriers = response.json()['data']['couriers']  # response.json() gives the response content in a dictionary so we can select the list of couriers

# with open(couriers_file, 'w') as out_file:
#     for item in list_of_couriers:
#         json.dump(item, out_file)   # dump() method converts a dictionary object into a JSON string
#         out_file.write('\n')        # insert a new line
#
#
# out_file.close()

print('Finished exporting the file')

#########################################################################
# If we need just exporting few of the fields available into a json file:
# 1. select the fields required
# 2. create a dictionary with them
# 3. dump into a json file

# Example:
           # define a dictionary variable
with open(couriers_file, 'w') as out_file:
    for item in list_of_couriers:
        key = item['slug']
        name = item['name']
        courier_dict = dict()
        courier_dict[key] = name    # create key: value pair from each item in the list of couriers
        json.dump(courier_dict, out_file)
        out_file.write('\n')

out_file.close()


