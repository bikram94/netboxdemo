import pynetbox
#import ipdb
import requests
import json

requests.packages.urllib3.disable_warnings()

session = requests.Session()
session.verify = False

nb = pynetbox.api(url="http://127.0.0.1:8000/", token="0123456789abcdef0123456789abcdef01234567")


dev = input("Enter your device name:")

is_dev = nb.dcim.devices.get(name=dev)

if is_dev:
    is_dev.delete()
    print(f'{dev} is deleted.')

else:

    print(f'{dev} doesn\'t exit')