import socket
import keyboard


sock = socket.socket()
sock.connect(('127.0.0.1', 8082))

sock.send(str.encode('name:qwerty1029;'))