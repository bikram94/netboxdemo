import requests
import json
import pynetbox

requests.packages.urllib3.disable_warnings()

#
token = "04df9580edd6ad6f18e9372c04589dd1b8971e1f"

# #data = {"id": 1, "status": "offline"}
#
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


id = 5

url = 'http://127.0.0.1:8000/api/dcim/devices/{}/'.format(id)

headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}

r = requests.delete(url=url,  headers=headers)

print(r.text)

