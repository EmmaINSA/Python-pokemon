import pygame
from pygame.locals import *
from Constants import *
from random import randint

pygame.init()

def loadMap():
    print("Not implemented yet !")

def formatText(textStr):

    # formated = pygame.Surface()

    splittext = textStr.split(" ")
    result = [[splittext[0]]]       # découper encore
    long = FONT.size(splittext[0])[0]
    line_iterator = 0

    for i in range (1, len(splittext)):
        long += FONT.size(splittext[i])[0]

        if long > MAX_TEXT_SIZE[0]:
            result.append([splittext[i]])
            # ajouter nouveau tableau
            # mettre le premier mot qui dépasse dedans
            long = 0
            line_iterator += 1
        else:
            result[line_iterator].append(splittext[i])

    result[line_iterator].append(splittext[i])


    # size = FONT.size(textStr)       # taille nécessaire en px pour afficher le texte donné
    # # dans la font sur laquelle on applique size
    #
    # final_text = [[splittext[0]]]

    # return size
    return result

def sumSize(str_list):
    size = (0,0)
    for item in str_list:
        size = tuple(map(sum, zip(FONT.size(item), size)))
    return size


def printText(text):
    formated = formatText(text)

    return True


""" ------ LES FONCTIONS USELESS MAIS SYMPA QUAND MEME ------
"Il faut mettre des petits Easter Eggs !" Yann 06/03/2018" 
"Un bon binage vaut deux arrosages !" Dicton """

def pingPong(argument):
    return argument

def fortyTwo():
    return 42

def randomYTP():
    quotes = ["Un boeuf !","Une fraise !","Mon petit, cette paix est ce pourquoi luttent tous les vrais guerriers.",
              "Inimaginable !", "Oooooh !", "Un énorrrme râteau", "Tout à coup ya un tas de sel", "Oskour oskour !",
              "Ils sont dans les villes, dans les campagnes !", "NON", "Pleeeein de spaghettis !",
              "La boule magique ! La boule de lavage, avec vos vêtements !", "Seul Link peut vaincre Ganon...",
              "Nieuheuheuheuh !", "C'est Boswer qui nous écrit !", "Squalala !", "N'est-ce pas ??"]
    return quotes[randint(0, len(quotes)-1)]