from Constants import *
from Map import *
from Objet_v1_6 import *
import pygame
from pygame.locals import *


map = Map("Files/pkmn_center.png",  PKMN_CENTER_CELLS)  #"Files/Music/mortal_stampede.ogg",

pkmn_center_2 = Map("Files/pkmn_center.png", PKMN_CENTER_CELLS_V2)

dawn = Personnage(pathList=DAWN_PATHLIST, pos=(7,5))

joelle = Objet("Files/infirmiere.png", JOELLE_POS)

screenMultip = 3