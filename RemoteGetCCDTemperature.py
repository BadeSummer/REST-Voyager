from connect import connect_to_vas, send_request, receive_response, disconnect_from_vas, find_event
import uuid

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

response_lines = receive_response(sock)

response_data = find_event(response_lines, "RemoteGetCCDTemperature")

print(f"CCD Temperature: {response_data.get('ParamRet').get('CCDTemp')}")