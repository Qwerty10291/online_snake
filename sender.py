import socket
import keyboard


sock = socket.socket()
sock.connect(('127.0.0.1', 8082))

sock.send(str.encode('hello world'))

keyboard.add_hotkey('w', lambda: sock.send(str.encode('w')))
keyboard.add_hotkey('a', lambda: sock.send(str.encode('a')))
keyboard.add_hotkey('s', lambda: sock.send(str.encode('s')))
keyboard.add_hotkey('d', lambda: sock.send(str.encode('d')))
keyboard.add_hotkey('r', lambda: print(bytes.decode(sock.recv)))
keyboard.wait()