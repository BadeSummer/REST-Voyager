import socket
import json


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
    

def disconnect_from_vas(sock):
    close_request = {
        'method': 'disconnect',
        'id' : 1
    }
    send_request(sock, close_request)
    close_respone = receive_response(sock)
    close_lines = close_response.split('\r\n')
    if close_respone['result'] == 0:
        return "Close safety"
    else:
        return f"Error with close connect: {close_respone}"