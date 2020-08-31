import pygame, sys, random, keyboard


#основной класс змеи
class Snake:
    def __init__(self, display, bodies, move, color):
        self.color = color
        self.rects = [pygame.Rect(i[0], i[1]) for i in bodies]
        self.display = display
        self.move = move
        self.vectors = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
        self.score = len(self.rects)
        self.borders = [pygame.Rect(0, -2, 1000, 1), pygame.Rect(1000, 0, 1, 700), pygame.Rect(0, 701, 1000, 1), pygame.Rect(-1, 0, 1, 700)]
    #метод отрисовки
    def draw(self, apple):
        self.move_snake(apple)
        x = self.rects[0].x
        y = self.rects[0].y
        #рисование глаз
        for i in self.rects:
            pygame.draw.rect(self.display, self.color, i)
        if  self.move == 'UP':
            pygame.draw.rect(self.display, (255, 0, 0), (x + 2, y + 2, 2, 2))
            pygame.draw.rect(self.display, (255, 0, 0), (x + 6, y + 2, 2, 2))
        elif self.move == 'RIGHT':
            pygame.draw.rect(self.display, (255, 0, 0), (x + 6, y + 2, 2, 2))
            pygame.draw.rect(self.display, (255, 0, 0), (x + 6, y + 6, 2, 2))
        elif self.move == 'DOWN':
            pygame.draw.rect(self.display, (255, 0, 0), (x + 2, y + 6, 2, 2))
            pygame.draw.rect(self.display, (255, 0, 0), (x + 6, y + 6, 2, 2))
        elif self.move == 'LEFT':
            pygame.draw.rect(self.display, (255, 0, 0), (x + 2, y + 2, 2, 2))
            pygame.draw.rect(self.display, (255, 0, 0), (x + 2, y + 6, 2, 2))
    
    
    #функция движения и проверки столкновений с обьектами
    def move_snake(self, apple):
        #проверка столкновения с телом
        for i in self.rects[1:]:
            if self.rects[0].move(self.vectors[self.move]).colliderect(i):
                sys.exit()
        
        #проверка столкновений со стенами
        if self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[0]):
            self.rects[0].move_ip(0, 690)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[1]):
            self.rects[0].move_ip(-990, 0)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[2]):
            self.rects[0].move_ip(0, -690)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[3]):
            self.rects[0].move_ip(990, 0)

        #проверка столкновения с яблоком
        if self.rects[0].move(self.vectors[self.move]).colliderect(apple):
            self.score += 1
            print(self.score)
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects
        else:
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects[:-1]

    
    #смена напрвления движения
    def change_direction(self, direction):
        if self.move == 'DOWN' and direction != 'UP':
            self.move = direction
        elif self.move == 'UP' and direction != 'DOWN':
            self.move = direction
        elif self.move == 'RIGHT' and direction != 'LEFT':
            self.move = direction
        elif self.move == 'LEFT' and direction != 'RIGHT':
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
    
    def check_collision(self, rect):
        return self.rect.colliderect(rect)



#инициализация pygame
pygame.init()
display = pygame.display.set_mode((1000, 700))
pygame.event.get()

#создание основных классов
snake = Snake(display, [[(200 - i * 10, 200), (10, 10)] for i in range(85)], 'RIGHT', (0, 255, 0))
apple = Apple(display, random.randint(1, 100) * 10, random.randint(1, 70) * 10, (255, 0, 0))
clock = pygame.time.Clock()

#привязка клавиш управления
keyboard.add_hotkey('up', lambda: snake.change_direction('UP'))
keyboard.add_hotkey('left', lambda: snake.change_direction('LEFT'))
keyboard.add_hotkey('down', lambda: snake.change_direction('DOWN'))
keyboard.add_hotkey('right', lambda: snake.change_direction('RIGHT'))


#главный цикл
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

