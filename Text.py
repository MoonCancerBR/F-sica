import pygame

class Text:
    def __init__(self, text, position, color, font_size=36, font_name=None):
        self.text = text
        self.position = position
        self.color = color
        self.font = pygame.font.Font(font_name, font_size)

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.position)