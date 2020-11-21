from model import Board
import pygame
import math
from pygame import gfxdraw

"""
Display a smooth circle
"""
def draw_circle(surface, x, y, radius, color):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color)

color = {
    "brown" : (139,69,19),
    "middle_brown" : (210,105,30),
    "dark_brown" : (89, 19, 0),
    "gold" : (255,215,0),
    "black": (0,0,0),
    "white" : (255,255,255),
}

class UIBoard(Board):
    def __init__(self, color_map = None):
        super().__init__()

        self.pawn_size = 32
        self.pawn_radius = self.pawn_size // 2
        self.res_size = self.pawn_size // self.row_size
        self.res_radius = self.res_size // 2

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

    def draw(self, surf, moves = None):
        board_width = (self.row_size + 1) * self.pawn_size + 2 # +1 for the result
        board_height = self.pawn_size * (self.max_row + 1) # +1 for the solution

        # Step 1 : Draw the board
        pygame.draw.rect(surf, color["brown"], (0, 0, board_width - self.pawn_size, board_height))
        pygame.draw.rect(surf, color["middle_brown"], (board_width - self.pawn_size, 0, self.pawn_size, board_height))

        # Step 2 draw the line between rows
        for i in range(0, self.max_row):
            pygame.draw.rect(surf, color["gold"], (0, i * self.pawn_size, board_width, 2))

        # Step 3 draw the pawns and result
        for i in range(0, len(self.rows)):
            # Pawns
            for j in range(0, len(self.rows[i])):
                draw_circle(surf, 
                            j * self.pawn_size + self.pawn_radius,
                            i * self.pawn_size + self.pawn_radius, 
                            self.pawn_radius,
                            self.color_map.get(self.rows[i][j])
                        )
            # Result
            for j in range(0, self.res[i] ["good"]):
                x = (self.row_size * self.pawn_size) + j * self.res_size + self.res_radius
                y = (i * self.pawn_size) + math.floor(self.pawn_size * 1 / 3)

                draw_circle(surf, x, y, self.res_radius, color["black"])

            for j in range(0, self.res[i] ["wrong"]):
                x = (self.row_size * self.pawn_size) + j * self.res_size + self.res_radius
                y = (i * self.pawn_size) + math.floor(self.pawn_size * 2 / 3)

                draw_circle(surf, x, y, self.res_radius, color["white"])

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

        # Step 6 (optionnal) : Display all possible move
        if moves != None:
            sol_pawn_size = 8
            sol_pawn_radius = sol_pawn_size // 2

            y_max = surf.get_rect().height - 2 * sol_pawn_size

            for i in range(0, len(moves)):
                for j in range(0, len(moves[i])):
                    y = (i * sol_pawn_size + sol_pawn_radius)
                    x = (board_width) + (j * sol_pawn_size + sol_pawn_radius)
                    # Add offset to column change
                    x = x + (math.floor(1.5 * len(moves[i]) * sol_pawn_size)) * math.floor(y / y_max)
                    y = y % y_max
                    
                    draw_circle(surf,x,y,sol_pawn_radius,self.color_map.get(moves[i][j]))