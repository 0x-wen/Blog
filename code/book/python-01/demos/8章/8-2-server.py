import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)

print("wait for connecting...")

conn, addr = server.accept()
print("接收到连接：", addr)
data = conn.recv(1024).decode("utf-8")
print("接收客户端数据：", data)
conn.send(data.upper().encode("utf-8"))
conn.close()




