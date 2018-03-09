from Constants import *


class Objet:

    """ Pour tout element qui sera affiché

    A ajouter :
        - animation / plusieurs sprites
        - convertir la pathlist une seule fois et la stocker dans une liste ?
    """

    def __init__(self, spritePath=None, pos=ORIGIN_POS, size=None, transparentColor=None):

        self.sprite = pygame.image.load(DEFAULT_SPRITE)

        self.size = size

        if spritePath is not None:
            self.spritePath = spritePath
            self.sprite = pygame.image.load(spritePath).convert_alpha()

            if transparentColor is not None:
                self.sprite.set_colorkey(transparentColor)

        self.pos = pos     # pos = case haut-gauche du sprite


    def get_rekt(self):
        print("Rectangle in ur face !")

    def afficher(self):
        fenetre.blit(self.sprite, (self.pos[0]*16, self.pos[1]*16))


class ObjetQuiBouge(Objet):     # herite de Objet

    def __init__(self, sprite=None, pathList=None, pos=ORIGIN_POS, size=None, transparentColor=None):

        Objet.__init__(self, spritePath=sprite, pos=pos, transparentColor=transparentColor)
        self.state = "still"    # useless for now
        self.direction = DOWN
        self.pathList = pathList
        self.canmove = True

        # self.sprite = pygame.image.load("Files/Poukebol.png")

        if pathList is not None:
            self.sprite = pygame.image.load(pathList[3]).convert_alpha()      # sprite de base = vers le bas

        elif sprite is not None:
            if transparentColor is not None:
                self.sprite = pygame.image.load(sprite)
                self.sprite.set_colorkey(transparentColor)
            else:
                self.sprite = pygame.image.load(sprite).convert_alpha()

        self.size = self.sprite.get_rect()

    """ ---------- DEBUT DU BORDEL ---------- """

    def canMoveUp(self, map_cells):
        if self.pos[1] > 0 and self.canmove:
            return map_cells[self.pos[1] - 1][self.pos[0]] in WALKABLE_CELLS
        else:
            return False

    def canMoveDown(self, map_cells):
        if self.pos[1] < len(map_cells)-1 and self.canmove:
            return map_cells[self.pos[1] + 1][self.pos[0]] in WALKABLE_CELLS
        else:
            return False

    def canMoveRight(self, map_cells):
        if self.pos[0] < len(map_cells[0])-1 and self.canmove:
            return map_cells[self.pos[1]][self.pos[0] + 1] in WALKABLE_CELLS
        else:
            return False

    def canMoveLeft(self, mapCells):
        if self.pos[0] > 0 and self.canmove:
            return mapCells[self.pos[1]][self.pos[0] - 1] in WALKABLE_CELLS
        else:
            return False

    """ ---------- FIN DU BORDEL ---------- """

    def move(self, direction, speed=10):      # speed ?

        if direction == LEFT:
            self.pos = (self.pos[0]-1, self.pos[1])
        elif direction == RIGHT:
            self.pos = (self.pos[0]+1, self.pos[1])
        elif direction == UP:
            self.pos = (self.pos[0], self.pos[1]-1)
        elif direction == DOWN:
            self.pos = (self.pos[0], self.pos[1]+1)

    def turn(self, direction):
        if self.canmove:
            if self.pathList is not None:
                self.sprite = pygame.image.load(self.pathList[direction]).convert_alpha()
            self.direction = direction


class Personnage(ObjetQuiBouge):

    def __init__(self, sprite=None, pathList=None, pos=ORIGIN_POS, size=None, transparentColor=None):
        ObjetQuiBouge.__init__(self, sprite, pathList, pos, size, transparentColor)



class ObjetQuiTourne(Objet):

    def __init__(self, spriteList, pos=ORIGIN_POS, transparentColor=None):
        Objet.__init__(self,spritePath=None, pos=pos, size=None, transparentColor=transparentColor)
