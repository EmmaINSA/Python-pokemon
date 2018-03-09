import pygame
from Constants import *

fenetre = pygame.display.set_mode(WINDOW_SIZE)

class Map:

    # gérer music = None

    def __init__(self, bgPath, musicPath=None, cells=None):
        self.fond = pygame.image.load(bgPath).convert()

        """
        if musicPath is not None:
            self.music = pygame.mixer.Sound(musicPath)
        else:
            self.music = None
        self.cells = cells
        """

    def playMusic(self):
        if self.music is not None:
            self.music.play()

    def stopMusic(self):
        if self.music is not None:
            self.music.stop()