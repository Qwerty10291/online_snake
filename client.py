import pygame, sys, keyboard, time, socket, random, json
from apple import Apple
from snake import Snake


# инициализация pygame
pygame.init()
display = pygame.display.set_mode((1000, 700))
pygame.event.get()
font = pygame.font.Font('14722.ttf', 36)
clock = pygame.time.Clock()
enemy = []

def sender(text):
    sock.send(str.encode(text))


def get_text():
    return bytes.decode(sock.recv(2048))

def handler(command):
    for i in command:
        if 'apple' in i:
            coords = i.split(':')[0]
            apple.change_position(coords.split(',')[0], coords.split(',')[1])
        if 'vector' in i:
            pass
        if 'snake' in i:
            rect = json.loads(i.split(':')[1])
            enemy.append(Snake(display, rect, 'RIGHT', (random.randint(10)))


# создание основных классов
snake = Snake(display, [[(200 - i * 10, 200), (10, 10)] for i in range(85)], 'RIGHT', (0, 255, 0))
apple = Apple(display, 10, 10, (255, 0, 0))
clock = pygame.time.Clock()

# инициализация socket
sock = socket.socket()
sock.connect(('127.0.0.1', 8085))
sock.send(str.encode(input()))
commands = get_text().split(';')
handler()






# привязка клавиш управления
keyboard.add_hotkey('up', lambda: snake.change_direction('UP'))
keyboard.add_hotkey('left', lambda: snake.change_direction('LEFT'))
keyboard.add_hotkey('down', lambda: snake.change_direction('DOWN'))
keyboard.add_hotkey('right', lambda: snake.change_direction('RIGHT'))

# главный цикл
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    display.fill((0, 0, 0))
    apple.draw()
    snake.draw(apple)
    if apple.check_collision(snake.rects[0]):
        apple.change_position(random.randint(1, 99) * 10, random.randint(1, 69) * 10)
    pygame.display.update()
    clock.tick(9)
