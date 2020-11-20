from model import Board
import pygame
from pygame import gfxdraw

def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

color = {
    "brown" : (139,69,19),
    "dark_brown" : (89, 19, 0),
    "gold" : (255,215,0),
}

class UIBoard(Board):
    def __init__(self, color_map = None):
        super().__init__()

        self.pawn_size = 32
        self.pawn_radius = self.pawn_size // 2

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
            7 : (32, 32, 32), # Gray
            8 : (210, 40, 130), # Pink
        }

    def draw(self, surf, show_all_moves = False):
        board_width = self.row_size * self.pawn_size + 2
        board_height = self.pawn_size * (self.max_row + 1) # +1 for the solution

        # Step 1 : Draw the board
        pygame.draw.rect(surf, color["brown"], (0, 0, board_width, board_height))

        # Step 2 draw the line between rows
        for i in range(0, self.max_row):
            pygame.draw.rect(surf, color["gold"], (0, i * self.pawn_size, board_width, 2))

        # Step 3 draw the pawns
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                #pygame.draw.ellipse(surf, self.color_map.get(self.rows[i][j]), (j * self.pawn_size, i * self.pawn_size, self.pawn_size, self.pawn_size))
                draw_circle(surf, 
                            j * self.pawn_size + self.pawn_radius,
                            i * self.pawn_size + self.pawn_radius, 
                            self.pawn_radius,
                            self.color_map.get(self.rows[i][j])
                        )

        # Step 4 display the solution
        for i in range(0, len(self.solution)):
            draw_circle(surf, 
                            i * self.pawn_size + self.pawn_radius,
                            self.max_row * self.pawn_size + self.pawn_radius, 
                            self.pawn_radius,
                            self.color_map.get(self.solution[i])
                        )

        # Step 5 cache solution
        pygame.draw.rect(surf, color["dark_brown"], (0, self.max_row * self.pawn_size, board_width, self.pawn_size *2/ 3))

        
        