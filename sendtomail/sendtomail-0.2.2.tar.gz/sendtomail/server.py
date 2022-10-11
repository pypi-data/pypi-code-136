import socket, urllib3, json
global debug
debug = "off"
protected = " Protected by: He1Zen, v1.0"

class server:
    def send(region:str, email:str, *message:str):
        if debug == "on":
            print("[3%] Debug mode ON")
            print("[7%] Region "+region)
            print("[11%] Starting to get URL")
            print("[20%] Getting json from URL")
        url = "https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/https.json"
        http = urllib3.PoolManager()
        request = http.request('GET', url)
        data = json.loads(request.data.decode('utf8'))
        ip = str(data["mailip"])
        port = int(data["mailport"])
        request = http.request('GET', "https://api.ipify.org/")
        my_ip = request.data.decode('utf8')
        if debug == "on":
            print("[40%] URL json data decode")
        if debug == "on":
            print("[60%] Server IP "+ip+":"+str(port))
            print("[65%] My IP: "+my_ip)
            print("[70%] Checking IP on blacklist")
        message = " ".join([str(m) for m in message])
        check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        check.connect((ip, port))
        check.sendall(bytes("free|check|ip|"+my_ip,'UTF-8'))
        code = check.recv(4096)
        get = code.decode('utf-8')
        check.shutdown(socket.SHUT_RDWR)
        check.close()
        if get == "blacklisted":
            return "Access denied, you ip address blacklisted!"+protected
        elif get == "tor":
            return "Access denied, please disable tor!"+protected
        elif get == "vpn" or get == "proxy":
            return "Access denied, please disable vpn!"+protected
        else:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, port))
            if debug == "on":
                print("[80%] Server connected!")
            client.sendall(bytes("smtp|"+region+"|"+email+"|"+message,'UTF-8'))
            if debug == "on":
                print("[98%] Data send to server")
            code = client.recv(4096)
            code = code.decode('utf-8')
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            return code
    def mail():
        if debug == "on":
            print("[7%] Debug mode ON")
            print("[11%] Starting to get URL")
            print("[20%] Getting json from URL")
        url = "https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/https.json"
        http = urllib3.PoolManager()
        request = http.request('GET', url)
        data = json.loads(request.data.decode('utf8'))
        if debug == "on":
            print("[40%] URL json data decode")
        ip = str(data["mailip"])
        port = int(data["mailport"])
        if debug == "on":
            print("[60%] Server IP "+ip)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        if debug == "on":
            print("[80%] Server connected!")
        client.sendall(bytes("get|free|mail|account",'UTF-8'))
        if debug == "on":
            print("[98%] Data send to server")
        free = client.recv(4096)
        free = free.decode('utf-8')
        free = json.loads(free)
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        return free
    def validate(email:str):
        url = "https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/https.json"
        http = urllib3.PoolManager()
        request = http.request('GET', url)
        data = json.loads(request.data.decode('utf8'))
        ip = str(data["mailip"])
        port = int(data["mailport"])
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.sendall(bytes("free|email|validation|"+email,'UTF-8'))
        check = client.recv(1024)
        check = check.decode('utf-8')
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        return check
    def regions():
        return "SMTP regions: us, uk, de, ua, ru, tr"
    def debug(type:str):
        global debug
        if type == "on":
            debug = "on"
        else:
            debug = "off"

