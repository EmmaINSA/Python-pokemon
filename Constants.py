from pygame.locals import *
import pygame

pygame.init()

LUCUS_BGCOLOR = (4,254,4)
DAWN_BGCOLOR = (136,184,176)
JOELLE_POS = (119,44)
ORIGIN_POS = (0,0)
PLAYER_ORIGIN = (112, 100)
MVT_UNIT = 8
WINDOW_SIZE = (256,192)
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
DEFAULT_SPRITE = "Files/Poukebol.png"
DAWN_PATHLIST = ["Files/Dawn/Dawn_Left.png",'Files/Dawn/Dawn_Back.png',"Files/Dawn/Dawn_Right.png","Files/Dawn/Dawn_Front.png"]
MVT_KEYS = [K_LEFT,K_RIGHT,K_UP,K_DOWN]

PKMN_CENTER_CELLS = [["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
                     ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
                     ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
                     ["P", "P", "P", "P", "P", "P", "P", "M", "M", "P", "P", "P", "M", "M", "M", "P"],
                     ["M", "M", "M", "M", "M", "P", "P", "P", "P", "P", "P", "M", "M", "M", "M", "P"],
                     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                     ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                     ["P", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "P"],
                     ["P", "P", "P", "P", "P", "P", "P", "T", "T", "P", "P", "P", "P", "P", "P", "P"]]

PKMN_CENTER_CELLS_V2 = [["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
                        ["P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P"],
                        ["P", "P", "P", "P", "P", "P", "P", "M", "M", "P", "P", "P", "P", "P", "P"],
                        ["M", "M", "M", "M", "P", "P", "P", "M", "M", "P", "P", "P", "M", "M", "M"],
                        ["M", "M", "M", "M", "P", "P", "P", "P", "P", "P", "P", "M", "M", "M", "M"],
                        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"],
                        ["P", "M", "M", "M", "M", "M", "M", "TD", "M", "M", "M", "M", "M", "M", "P"],]

PKMN_CENTER_OFFSET = (8,4)

WALKABLE_CELLS = ('M','TL','TD','TU','TR')

TEXTBOX_POS = (3,147)
TEXT_POS = (14, 150)
MAX_TEXT_SIZE = (225,38)

FONT = pygame.font.SysFont("monospace", 15, bold=True)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," \
              " sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
              " Ut enim ad minim veniam," \
              " quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat." \
              " Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur." \
              " Excepteur sint occaecat cupidatat non proident," \
              " sunt in culpa qui officia deserunt mollit anim id est laborum."