import pygame, sys, random


#основной класс змеи
class Snake:
    def __init__(self, display, bodies, move, color):
        self.color = color
        self.rects = [pygame.Rect(i[0], i[1]) for i in bodies]
        self.display = display
        self.move = move
        self.vectors = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
    
    #метод отрисовки
    def draw(self, apple):
        self.move_snake(apple)
        for i in self.rects:
            pygame.draw.rect(self.display, self.color, i)
    
    
    #функция движения
    def move_snake(self, apple):
        if self.rects[0].colliderect(apple):
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects
        else:
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects[:-1]
    
    #смена напрвления движения
    def change_direction(self, direction):
        print(self.move)
        if self.move == 'DOWN' and direction != 'UP':
            print('down')
            self.move = direction
        elif self.move == 'UP' and direction != 'DOWN':
            print('UP')
            self.move = direction
        elif self.move == 'RIGHT' and direction != 'LEFT':
            print('RIGHT')
            self.move = direction
        elif self.move == 'LEFT' and direction != 'RIGHT':
            print('LEFT')
            self.move = direction

class Apple:
    def __init__(self, display, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 10, 10)
        self.display = display

    def draw(self):
        pygame.draw.rect(self.display, self.color, self.rect)

    def change_position(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)

    def check_collision(self, rects):
        return self.rect.colliderect(rects)



#инициализация pygame
pygame.init()
display = pygame.display.set_mode((1000, 700))
pygame.event.get()

#создание основных классов
snake = Snake(display, [[(200 - i * 10, 200), (10, 10)] for i in range(3)], 'RIGHT', (0, 255, 0))
apple = Apple(display, random.randint(1, 100) * 10, random.randint(1, 70) * 10, (255, 0, 0))
clock = pygame.time.Clock()


#главный цикл
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.change_direction('UP')
    elif keys[pygame.K_DOWN]:
        snake.change_direction('DOWN')
    elif keys[pygame.K_RIGHT]:
        snake.change_direction('RIGHT')
    elif keys[pygame.K_LEFT]:
        snake.change_direction('LEFT')
    display.fill((0, 0, 0))
    apple.draw()
    snake.draw(apple)
    if apple.check_collision(snake.rects[0]):
        apple.change_position(random.randint(1, 99) * 10, random.randint(1, 69) * 10)
    pygame.display.update()
    clock.tick(10)

