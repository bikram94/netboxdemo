import pynetbox
#import ipdb
import requests
import json

requests.packages.urllib3.disable_warnings()

session = requests.Session()
session.verify = False

token = "04df9580edd6ad6f18e9372c04589dd1b8971e1f"

nb = pynetbox.api(url="http://127.0.0.1:8000/", token=token)
# Specify number of Spine and Leaf switches
SPINE_NUM = 2
LEAF_NUM = 8

# List to store dictionaries with attributes for new devices
melb_devices = list()

print(nb.dcim.device_roles.get)

# Retrieve objects needed for creation of Melbourne devices
site_toronto = nb.dcim.sites.get(slug="dc2")
drole_leaf = nb.dcim.device_roles.get(slug="Leaf-Switch")
drole_spine = nb.dcim.device_roles.get(slug="Spine-Switch")
dtype_ar7060 = nb.dcim.device_types.get(slug="Arista")
dtype_ar7280 = nb.dcim.device_types.get(slug="Arista")

print(site_toronto)



list_url = 'http://127.0.0.1:8000/api/dcim/devices/'


headers = {'Authorization': "Token {}".format(token), 'content-type': "application/json"}


#### Listing Devices #####

r = requests.get(url=list_url,  headers=headers)

result = r.json()['results']

dev_list = list()

for dev in result:

    dev_type = dev['device_type']['id']
    dev_role_id =  dev['device_role']['id']
    dev_role = dev['device_role']['display']
    dev_site_id = dev['site']['id']

    if "leaf" in dev_role.lower():
        leaf_type_id = dev['device_type']['id']
        leaf_role_id = dev['device_role']['id']

    elif "spine" in dev_role.lower():

        spine_type_id = dev['device_type']['id']
        spine_role_id = dev['device_role']['id']

    else:
        pass

print("leaf_type_id {0}, leaf_role_id {1}, spine_type_id {2}, spine_role_id {3}".format(leaf_type_id,leaf_role_id,spine_type_id,spine_role_id ))

# Generate attributes for spines
for i in range(1, SPINE_NUM + 1):
    melb_devices.append(
        dict(
            name="sw-spine-toronto-0{swid}".format(swid=i),
            device_type=spine_type_id,
            device_role=spine_role_id,
            site=site_toronto.id,
        )
    )

# Generate attributes for leaves
for i in range(1, LEAF_NUM + 1):
    melb_devices.append(
        dict(
            name="sw-leaf-toronto-0{swid}".format(swid=i),
            device_type=leaf_type_id,
            device_role=leaf_role_id,
            site=site_toronto.id,
        )
    )

try:
    # Try creating all of the devices at once
    results = nb.dcim.devices.create(melb_devices)



    # Set formatting and header
    fmt = "{:<25}{:<15}{:<15}{:<15}"
    header = ("Device", "Dev Role", "Dev Type", "Site")

    # Print header
    print(fmt.format(*header))

    # Print summary info for each of the devices
    for r in results:
        print(
            fmt.format(
                r["name"],
                r["device_role"]["name"],
                r["device_type"]["model"],
                r["site"]["name"],
            )
        )

    # # As a bonus, dump to json file objects returned by NetBox
    # with open("melbourne_devices.json", encoding="utf-8", mode="w") as fout:
    #     json.dump(results, fout)

except Exception as e:
    print(e)