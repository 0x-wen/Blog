import socket
from concurrent.futures import ThreadPoolExecutor

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)


def handle(conn, addr):
    print("接收到连接：", addr)
    data = conn.recv(1024).decode("utf-8")
    if not data:
        return
    print("接收客户端数据：", data)
    conn.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))
    current_path = data.split(' ')[1]
    if current_path == "/index":
        conn.send("<h1>hello index<h1>".encode("utf-8"))
    elif current_path == "/about":
        conn.send("<h1>hello about<h1>".encode("utf-8"))
    else:
        conn.send("<h1>hello web<h1>".encode("utf-8"))
    conn.close()


pool = ThreadPoolExecutor(5)

while 1:
    print("wait for connecting...")
    conn, addr = server.accept()
    # 从线程池回去worker,执行handle任务
    pool.submit(handle, conn, addr)




