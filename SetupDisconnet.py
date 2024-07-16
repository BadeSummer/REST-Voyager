from connect import connect_to_vas, send_request, receive_response, find_event
import uuid
import time
uid = str(uuid.uuid4())

sock = connect_to_vas()

request = {
    "method": "RemoteSetupDisconnect",
    "params": {
        "UID": uid,
        "TimeoutDisconnect": 10
        },
    "id": 1
}

send_request(sock, request)

time.sleep(1)
response_lines = receive_response(sock)
print(response_lines)
response_data = find_event(response_lines, "RemoteActionResult")
# disconnect_from_vas(sock)