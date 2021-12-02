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
# nb = pynetbox.api(url="http://127.0.0.1:8000/", token="a1d4293f44d220ff798c6768573b087bc4c45781")
#
#
# dev = input("Enter your device name:")
#
# is_dev = nb.dcim.devices.get(name=dev)
#
# if is_dev:
#
#     dev_serial = is_dev.serial
#
#     is_dev.serial = '1234'
#
#     is_dev.save()
#
#     print(dev_serial)
#     #
#     print(f'{dev} serial is modified.')
#
# else:
#
#     print(f'{dev} doesn\'t exit')


token = "04df9580edd6ad6f18e9372c04589dd1b8971e1f"

url = 'http://127.0.0.1:8000/api/dcim/devices/'

del_url = 'http://127.0.0.1:8000/api/dcim/devices/{}/'.format(id)


headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}


serial_num = 12345


#### Listing Devices #####

r = requests.get(url=url,  headers=headers)

result = r.json()['results']

dev_list = list()

for dev in result:

    dev_list.append(int(dev['id']))

    print(dev)


print(dev_list)


for id in dev_list:

    patch_url = 'http://127.0.0.1:8000/api/dcim/devices/{}/'.format(id)

    data = {"serial": serial_num, "status": "offline"}

    #data = {"Status": "Offline"}

    r = requests.patch(url=patch_url, headers=headers, data=json.dumps(data))

    print(r.status_code)

    print(" A device with ID {} is modified".format(id))

    serial_num = serial_num + 1
