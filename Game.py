import pygame
from Position import Position
from Vector import Vector
from  Color import Colors
from Text import Text

class Game:

    def __init__(self):
        self.player_pos = Position(50, 500 )
        self.player_speed_mag = 15
        self.player_speed = Vector(0.5,-1)*self.player_speed_mag
        self.start = False
        self.gravity = Vector(0, 0.82)

    def update(self, delta_time):
        if self.start:
            #vetor aceleracao sendo aplicado ao vetor_speed
            # tem que ir sobrescrevendo para cada Delta_t
            self.player_speed = self.player_speed + self.gravity
            self.player_pos.translate(self.player_speed)
        # Lógica de atualização do jogo (ex: simulações físicas)
        pass

    def draw(self, screen):
        self.player_pos.draw(screen)
        text = Text("Hello, Pygame!", (0, 0), Colors.BLACK)
        text.draw(screen)
    def handle_event(self):
        keys = pygame.key.get_pressed()
        self.handle_keys(keys)

    def handle_keys(self, keys):
        if keys[pygame.K_SPACE]:
            self.start = True
        if keys[pygame.K_r]:
            self.reset()
        
    def reset(self):
        self.player_pos = Position(50, 500 )
        self.player_speed_mag = 15
        self.player_speed = Vector(1,-1)*self.player_speed_mag
        self.start = False
    