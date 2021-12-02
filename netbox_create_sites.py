import requests
import json

requests.packages.urllib3.disable_warnings()

# session = requests.Session()
# session.verify = False


token = "04df9580edd6ad6f18e9372c04589dd1b8971e1f"

data = [ {"name": "dc3", "slug": "dc3", "description": "Data Center in Toronto"}, {"name": "dc4", "slug": "dc4", "description": "Data Center in Edmonton"}]


url = 'http://127.0.0.1:8000/api/dcim/sites/'

headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}

r = requests.post(url=url,  headers=headers, data=json.dumps(data))

print(r.status_code)

