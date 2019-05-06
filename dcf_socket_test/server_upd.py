import socket

def Main():
    host = '127.0.0.1'
    port = 50010

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('message from: ' + str(addr))
        print('from connect user: ' + data)
        data = data.upper()
        print("Sending " + data)
        s.sendto(data.encode('utf-8'), addr)
    c.close()


if __name__ == "__main__":
    Main()
