# import pynetbox
# #import ipdb
import requests
import json
#
# requests.packages.urllib3.disable_warnings()
#
# session = requests.Session()
# session.verify = False
#
# nb = pynetbox.api(url="http://127.0.0.1:8000/", token="0123456789abcdef0123456789abcdef01234567")
# nb.http_session = session
#
# devices = nb.dcim.devices.all()
#
#
# for nb_device in devices:
#     platform = str(nb_device.platform)
#     pri_ip = str(nb_device.primary_ip)
#     asset = nb_device.device_role
#     site = nb_device.site.id
#     print (nb_device,platform,pri_ip,asset, site, nb_device.id)


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

    print(dev)


print(dev_list)


#### Deletion #####

for id in dev_list:

    del_url = 'http://127.0.0.1:8000/api/dcim/devices/{}/'.format(id)

    r = requests.delete(url=del_url, headers=headers)

    print(r.status_code)

    print("Device with ID {} is deleted".format(id))





