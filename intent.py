import requests
import json

ONOS_BASE_URL = "http://127.0.0.1:8181/onos/v1/" # onos ip:version

def create_intent(src_host, dst_host):
    intent_data = {
        "type": "HostToHostIntent",
        "appId": "org.onosproject.fwd",
        "one": src_host,
        "two": dst_host
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(ONOS_BASE_URL + "intents", data=json.dumps(intent_data), headers=headers)

    if response.status_code == 200:
        print("Intent made")
    else:
        print(f"Failed to make intent, http status code: {response.status_code}")
        print(response.text)

def main():
    src_host = "of:0000000000000001/1"  #source mac addr
    dst_host = "of:0000000000000002/1"  #dest mac addr

    # request
    create_intent(src_host, dst_host)

if __name__ == "__main__":
    main()
