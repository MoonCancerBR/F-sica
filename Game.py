import pygame
from  Color import Colors
from Text import Text
class Game:
    def __init__(self):
        self.player_pos = [400, 300]
        self.player_speed = 5


    def update(self, delta_time):
        # Lógica de atualização do jogo (ex: simulações físicas)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, Colors.BLUE, self.player_pos, 10)
        text = Text("Hello, Pygame!", (0, 0), Colors.BLACK)
        text.draw(screen)
    def handle_event(self):
        keys = pygame.key.get_pressed()
        self.handle_keys(keys)

    def handle_keys(self, keys):
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

    #-----------------PRIVATE-----------------------------
    def move_left(self):
        self.player_pos[0] -= self.player_speed

    def move_right(self):
        self.player_pos[0] += self.player_speed

    def move_up(self):
        self.player_pos[1] -= self.player_speed

    def move_down(self):
        self.player_pos[1] += self.player_speed

    
