from model import Board
import pygame

color = {
    "brown" : (139,69,19),
    "gold" : (255,215,0),
}

panw_size = 32

class UIBoard(Board):
    def __init__(self, color_map = None):
        super().__init__()
        self.color_map = color_map
        if self.color_map == None:
            self.load_default_color_map()

    def load_default_color_map(self):
        self.color_map = {
            1 : (255, 0, 0), # Red
            2 : (0, 255, 0), # Green
            3 : (0, 0, 255), # Blue
            4 : (255, 255, 0), # Yellow
            5 : (0, 255, 255), # Cyan
            6 : (255, 255, 255), # White
            7 : (64, 64, 64), # Gray
            8 : (210, 40, 130), # Pink
        }

    def draw(self, surf):
        # Step 1 : Draw the board
        pygame.draw.rect(surf, color["brown"], (0, 0, self.row_size * panw_size, panw_size * self.max_row))
        for i in range(0, self.max_row):
            pygame.draw.rect(surf, color["gold"], (0, i * panw_size, self.row_size * panw_size, 2))

        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                pygame.draw.ellipse(surf, self.color_map.get(self.rows[i][j]), (j * panw_size, i * panw_size, panw_size, panw_size))