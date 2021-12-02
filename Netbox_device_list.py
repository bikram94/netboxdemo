# import pynetbox
# #import ipdb
import requests
import json


token = "04df9580edd6ad6f18e9372c04589dd1b8971e1f"

url = 'http://127.0.0.1:8000/api/dcim/devices/'

del_url = 'http://127.0.0.1:8000/api/dcim/devices/{}/'.format(id)


headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}


#### Listing Devices #####

r = requests.get(url=url,  headers=headers)

result = r.json()['results']

dev_list = list()

for dev in result:

    dev_list.append(int(dev['id']))

    #print(dev)

    dev_name = dev['name']
    dev_id = dev['id']
    dev_type = dev['device_type']['id']
    dev_model = dev['device_type']['model']
    dev_role_id =  dev['device_role']['id']
    dev_role = dev['device_role']['display']
    dev_site_id = dev['site']['id']
    dev_site_name = dev['site']['display']


    print(" Device Name {0}, Device ID {1}, Device Type ID {2}, Model {3}, Device Role ID {4},  Device Role {5}, Site ID {6}, Site Name {7}".format(dev_name,dev_id, dev_type, dev_model,dev_role_id,dev_role,dev_site_id, dev_site_name)  )