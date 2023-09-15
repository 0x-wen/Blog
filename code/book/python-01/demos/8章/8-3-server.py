import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)

print("wait for connecting...")

while 1:
    conn, addr = server.accept()
    print("接收到连接：", addr)

    while 1:
        try:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            print("接收客户端数据：", data)
            conn.send(data.upper().encode("utf-8"))
        except Exception as e:
            print(e)
            break
    conn.close()




