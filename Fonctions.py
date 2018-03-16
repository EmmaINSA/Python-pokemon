from Constants import *
from random import randint

pygame.init()

def loadMap():
    print("Not implemented yet !")

def formatText(textStr):

    splittext = textStr.split(" ")
    # ajouter un espace à la fin de chaque mot ?
    result = [[[splittext[0]]]]
    long = FONT.size(splittext[0])[0]
    line = 0

    for i in range (1, len(splittext)):
        long += FONT.size(splittext[i])[0]

        if long > MAX_TEXT_SIZE[0]:
            if line%2:  # si numero ligne est impair (dernière ligne du bloc) -> on change de bloc
                result.append([[splittext[i]]])
            else:
                result[line//2].append([splittext[i]])

            long = FONT.size(splittext[i])[0]   # reset la taille

        else:
            result[line//2][line%2].append(splittext[i])

    # splittext = textStr.split(" ")
    # result = [[splittext[0]]]       # découper encore
    # long = FONT.size(splittext[0])[0]
    # line_iterator = 0
    #
    # for i in range (1, len(splittext)):
    #     long += FONT.size(splittext[i])[0]
    #
    #     if long > MAX_TEXT_SIZE[0]:
    #         result.append([splittext[i]])
    #         # ajouter nouveau tableau
    #         # mettre le premier mot qui dépasse dedans
    #         long = FONT.size(splittext[i])[0]       # ça marche mieux comme ça
    #         line_iterator += 1
    #     else:
    #         result[line_iterator].append(splittext[i])
    #
    # result[line_iterator].append(splittext[i])

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
              "Inimaginable !", "Oooooh !", "Un énorrrme râteau", "Tout à coup ya un tas de sel",
              "Oskour oskour ! J'ai mon bébé qui s'étouffe !",
              "Ils sont dans les villes, dans les campagnes !", "NON", "Pleeeein de spaghettis !",
              "La boule magique ! La boule de lavage, avec vos vêtements !", "Seul Link peut vaincre Ganon...",
              "Nieuheuheuheuh !", "C'est Boswer qui nous écrit !", "Squalala !", "N'est-ce pas ??",
              "Je vais appliquer des 'Calmez-vous !'"]
    return quotes[randint(0, len(quotes)-1)]
