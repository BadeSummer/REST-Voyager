from connect import connect_to_vas, send_request, receive_response, find_event, disconnect_to_vas
import uuid
import time
import json

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

uid = str(uuid.uuid4())

sock = connect_to_vas()

set_dashboard_mode_request = {
    "method": "RemoteSetDashboardMode",
    "params": {
        "UID": uid,
        "IsOn": "true"
        },
    "id": 2
}

send_request(sock, set_dashboard_mode_request)

control_data = None
count = 0
while (not control_data) and count < 3:
    time.sleep(1)
    response_lines = receive_response(sock)
    control_data = find_event(response_lines, "ControlData")
    if control_data:
        fn = os.path.join(SCRIPT_DIR, 'control_data.json')
        with open("control_data.json", "w") as f:
            f.write(json.dumps(control_data, indent=4))

        print(json.dumps(control_data, indent=4))
    else:
        count += 1

disconnect_to_vas(sock)