import socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.connect(('127.0.0.7', 8000))
skt.sendall('OK')

while True:
    data = skt.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data)

skt.close()        
