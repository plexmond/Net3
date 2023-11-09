import requests
import json

ONOS_BASE_URL = "http://172.17.0.5:8181/onos/v1/"  # onos:port
ONOS_USERNAME = "onos"
ONOS_PASSWORD = "rocks"

def create_intent(src_host, dst_host):
    intent_data = {
        "type": "HostToHostIntent",
        "appId": "org.onosproject.cli",
        "priority":'100',
        "one": src_host,
        "two": dst_host
    }

    headers = {"Content-Type": "application/json"}

    auth = (ONOS_USERNAME, ONOS_PASSWORD)

    response = requests.post(
        ONOS_BASE_URL + "intents",
        data=json.dumps(intent_data),
        headers=headers,
        auth=auth
    )

    if response.status_code == 201:
        print("Intent made")
    else:
        print(f"Failed to make intent, HTTP status code: {response.status_code}")
        print(response.text)

def main():
    src_host = "00:00:00:00:00:01/-1"  # source mac addr
    dst_host = "00:00:00:00:00:08/-1"  # dest mac addr

    # request
    create_intent(src_host, dst_host)

if __name__ == "__main__":
    main()
