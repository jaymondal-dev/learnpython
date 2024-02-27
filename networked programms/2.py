import socket
import time
host='data.pr4e.org'
port=80
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host,port))
mysock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")
picture=b""
count=0

while True:
    data=mysock.recv(5120)
    if len(data)<1: break
    time.sleep(0.25)
    count=count+len(data)
    print(len(data),count)
    picture=picture+data
mysock.close()
pos=picture.find(b"\r\n\r\n")
print("header length",pos)
print(picture[:pos].decode())
pictue=picture[pos+4:]
file=open("text.jpg","wb")
file.write(picture)
file.close()

