import socket
import json
import time

def set_up_connection():
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)
    json_file.close()
    return config


def connect_to_vas():
    config = set_up_connection()

    server_address = config.get("SERVER")
    port = config.get("PORT")

    try:
        # 创建一个TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接到服务器和端口
        sock.connect((server_address, port))

        # sleep to wait connetion to be established
        time.sleep(1)
        return sock
    
    except Exception as e:
        print(f"Error connecting to Voyager Application Server: {e}")
        return None
    
def send_request(sock, request):
    try:
        # 将请求转化为JSON格式的字符串
        request_str = json.dumps(request) + "\r\n"
        # 发送请求
        sock.sendall(request_str.encode('utf-8'))
    except Exception as e:
        print(f"Error sending request: {e}")


def find_event(lines, event_name):
    for line in lines:
        if line.strip():  # 忽略空行
            try:
                data = json.loads(line)
                if data.get("Event") == event_name:
                    return data
            except json.JSONDecodeError:
                print(f"Error decoding JSON: {line}")
    return None


def receive_response(sock):
    try:
        # 接收服务器的响应
        response = sock.recv(4096).decode('utf-8')

        lines = response.split('\r\n')

        return lines
    
    except Exception as e:
        print(f"Error receiving response: {e}")
        return None
    

def disconnect_to_vas(sock):
    close_request = {
        'method': 'disconnect',
        'id' : 1
    }
    send_request(sock, close_request)
    time.sleep(0.1)
    close_respone_lines = receive_response(sock)
    if close_respone_lines[-1].get('result') == 0:
        return "Close safety"
    else:
        raise Exception(f"Close failed: {close_respone_lines}")