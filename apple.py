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