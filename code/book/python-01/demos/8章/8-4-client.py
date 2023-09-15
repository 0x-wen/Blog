import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

while 1:
    cmd = input(">>>:").strip()
    if cmd == "q":
        break
    if not cmd:
        continue
    client.send(cmd.encode("utf-8"))
    data = client.recv(1024).decode("utf-8")
    print(data)

client.close()
