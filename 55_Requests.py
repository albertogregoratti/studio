import requests

req = requests.get('https://springer.cloud.looker.com/')

site_status = req.status_code
if site_status < 400:
    print('OK')
else: print ('Site down')
