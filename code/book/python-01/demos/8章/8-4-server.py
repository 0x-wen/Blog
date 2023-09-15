import socket
from concurrent.futures import ThreadPoolExecutor

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(5)


def handle(conn, addr):
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


pool = ThreadPoolExecutor(5)

while 1:
    print("wait for connecting...")
    conn, addr = server.accept()
    # 从线程池回去worker,执行handle任务
    pool.submit(handle, conn, addr)







