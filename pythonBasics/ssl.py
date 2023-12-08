## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests

import json
import requests

# added comment
FRESHDESK_ENDPOINT = "https://springeronlineservice.freshdesk.com" # check if you have configured https, modify accordingly
FRESHDESK_KEY = "7DdGXEYYL4ndy752"

#Example: /helpdesk/tickets/30.json
# r = requests.get(FRESHDESK_ENDPOINT + '/helpdesk/tickets/8232296.json', auth=(FRESHDESK_KEY, "X"))
r2 = requests.get("https://springeronlineservice.freshdesk.com/helpdesk/tickets/8232296", auth=(FRESHDESK_KEY, "X"))
#r = requests.get(FRESHDESK_ENDPOINT + '/helpdesk/tickets/8232296.json', auth=(FRESHDESK_KEY, "X"),
#                 verify="C:\\Users\\alberto.gregoratti\\AppData\\Roaming\\Python\\Python310\\site-packages\\certifi\\cacert.pem")


print ('HTTP response code: ' + str(r2.status_code))
print ('HTTP response body: ' + str(r2.content))

# added comment
# added comment 2