import socket, json, keyboard

adresses = {}

sock = socket.socket()
sock.bind(('127.0.0.1', 8082))
sock.listen(5)
while not keyboard.is_pressed('esc'):
	conn, adress = sock.accept()
	if adress not in adresses:
		adresses[adress] = [conn, ['wrf', 'sdoci']]

	while True:
		data = conn.recv(1024)
		if not data:
			break
		data = bytes.decode(data)
		conn.send(str.encode(json.dumps(adresses[adress][1])))
		print(data)
