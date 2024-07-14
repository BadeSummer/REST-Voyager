from connect import connect_to_vas, send_request, receive_response, find_event
import uuid
import time
uid = str(uuid.uuid4())

sock = connect_to_vas()

request = {
    "method": "RemoteGetCCDTemperature",
    "params": {
        "UID": uid
        },
    "id": 1
}

send_request(sock, request)

time.sleep(1)
response_lines = receive_response(sock)
print(response_lines)
response_data = find_event(response_lines, "RemoteActionResult")

print(f"CCD Temperature: {response_data.get('ParamRet').get('CCDTemp')}")

# disconnect_from_vas(sock)