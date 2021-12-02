
import pynetbox
#import ipdb
import requests
import json

requests.packages.urllib3.disable_warnings()

token = "a1d4293f44d220ff798c6768573b087bc4c45781"

nb = pynetbox.api(url="http://127.0.0.1:8000/", token="0123456789abcdef0123456789abcdef01234567")

url = 'http://127.0.0.1:8000/api/dcim/sites/'

headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}

r = requests.get(url,  headers=headers)

print(r.json())
