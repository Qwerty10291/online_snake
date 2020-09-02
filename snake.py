# основной класс змеи
class Snake:
    def __init__(self, display, bodies, move, color):
        self.color = color
        self.rects = [pygame.Rect(i[0], i[1]) for i in bodies]
        self.display = display
        self.move = move
        self.vectors = {'UP': (0, -10), 'DOWN': (0, 10), 'LEFT': (-10, 0), 'RIGHT': (10, 0)}
        self.score = len(self.rects)
        self.borders = [pygame.Rect(0, -2, 1000, 1), pygame.Rect(1000, 0, 1, 700), pygame.Rect(0, 701, 1000, 1),
                        pygame.Rect(-1, 0, 1, 700)]

    # метод отрисовки
    def draw(self, apple):
        self.move_snake(apple)
        x = self.rects[0].x
        y = self.rects[0].y
        # рисование глаз
        for i in self.rects:
            pygame.draw.rect(self.display, self.color, i)
        if self.move == 'UP':
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

    # функция движения и проверки столкновений с обьектами
    def move_snake(self, apple):
        # проверка столкновения с телом
        for i in self.rects[1:]:
            if self.rects[0].move(self.vectors[self.move]).colliderect(i):
                font = pygame.font.Font('14722.ttf', 36)
                self.display.blit(font.render('Game Over!', True, (255, 255, 255)), (400, 300))
                pygame.display.update()
                time.sleep(3)
                sys.exit()

        # проверка столкновений со стенами
        if self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[0]):
            self.rects[0].move_ip(0, 690)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[1]):
            self.rects[0].move_ip(-990, 0)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[2]):
            self.rects[0].move_ip(0, -690)
        elif self.rects[0].move(self.vectors[self.move]).colliderect(self.borders[3]):
            self.rects[0].move_ip(990, 0)

        # проверка столкновения с яблоком
        if self.rects[0].move(self.vectors[self.move]).colliderect(apple):
            self.score += 1
            print(self.score)
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects
        else:
            self.rects = [self.rects[0].move(self.vectors[self.move])] + self.rects[:-1]

    # смена напрвления движения
    def change_direction(self, direction):
        if self.move == 'DOWN' and direction != 'UP':
            self.move = direction
        elif self.move == 'UP' and direction != 'DOWN':
            self.move = direction
        elif self.move == 'RIGHT' and direction != 'LEFT':
            self.move = direction
        elif self.move == 'LEFT' and direction != 'RIGHT':
            self.move = direction