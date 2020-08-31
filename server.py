import socket, json, keyboard, random

adresses = []
users = {}
apple = [random.randint(1, 100) * 10, random.randint(1, 70) * 10]
commands = ''
sock = socket.socket()
sock.bind(('127.0.0.1', 8082))
sock.listen(5)

def handler(message, conn):
	global users
	message = message.split(';')
	for i in message:
		if 'name' in message:
			name = i.split(':')[1]
			users[name] = [[[(200 - i * 10, 200), (10, 10)] for i in rang]
		if 'apple' in message:


while not keyboard.is_pressed('esc'):
	conn, adress = sock.accept()
	if adress not in adresses:
		adresses.append(adress)
	while True:
		data = conn.recv(1024)
		if not data:
			break
		data = bytes.decode(data)
		commands += data
		print(data)
	if commands:

