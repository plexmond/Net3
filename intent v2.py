import requests
import json

url='http://172.17.0.5:8181/onos/v1/'

intent = {
     "type": "HostToHostIntent",
     "appId": "org.onosproject.cli",
     "priority":"100",
     "one":'00:00:00:00:00:01/-1',
     "two":'00:00:00:00:00:02/-1'
}

data = json.dumps(intent)

headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
}

response = requests.post(url + 'intents', headers=headers, data=data, auth=('onos', 'rocks'))

if response.status_code == 201:
     print('Success')
else:
     print("Failed", response.content)