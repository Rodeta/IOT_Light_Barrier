import requests
from requests.structures import CaseInsensitiveDict
#headers = CaseInsensitiveDict()
#headers["Accept"] = "application/json"
#headers["Content-Type"] = "application/json"
base_path = 'https://192.168.0.94:44378/api/parkingrow'
response = requests.get(base_path, verify=False)
print(response.status_code)
print(response.text)
update_path = 'https://192.168.0.94:44378/api/parkingrow/1'
headers = {"Content-Type": "application/json", "Accept":"application/json"}
data = {"increase":True}
patch_request = requests.patch(update_path, json=data, verify=False)
print(patch_request.status_code)
print(patch_request.text)
#patch_request = requests.patch(base_path + '/1',headers=headers, data={'increasing':True}, verify=False)
#print(patch_request.status_code)