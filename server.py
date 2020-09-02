import socket, json, keyboard, random

sock = socket.socket()
sock.bind(('127.0.0.1', 8085))
apple = [random.randint(0, 100) * 10, random.randint(0, 70)]
users = {}


class User:
	def __init__(self, conn, adress, nick:str, direction:str, rects:list):
		self.conn = conn
		self.adress = adress
		self.nick = nick
		self.direction = direction
		self.rects = rects
		self.score = len(rects)
	
	def change_direction(self, direction):
		self.direction = direction
	
	def add_score(self):
		self.rects += 1
	
	def add_rect(self, x, y):
		self.rects.append()


def init_user(self, conn):



def change_apple():
	global apple
	apple = [random.randint(0, 100) * 10, random.randint(0, 70)]


commands = 