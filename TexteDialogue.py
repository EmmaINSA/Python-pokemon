from Constants import *

class TexteDialogue:

    def __formatText(self, textStr):  # censé être privée ?
        # ＼(＾▽＾)／

        splittext = textStr.split(" ")
        # ajouter un espace à la fin de chaque mot ?
        result = [[[splittext[0]]]]
        long = self.font.size(splittext[0])[0]
        line = 0

        for i in range(1, len(splittext)):
            long += self.font.size(splittext[i])[0]

            if long > MAX_TEXT_SIZE[0]:
                if line % 2:  # si numero ligne est impair (dernière ligne du bloc) -> on change de bloc
                    result.append([[splittext[i]]])
                else :
                    result[line // 2].append([splittext[i]])

                long = self.font.size(splittext[i])[0]  # reset la taille
                line +=1

            else:
                result[line // 2][line % 2].append(splittext[i])

        return result

    def __init__(self, text, color=BLACK, font=FONT, textbox="Files/textbox_1.png"):
        self.text = text
        self.textbox = textbox
        self.color = color
        self.font = font
        self.formatedText = self.__formatText(text)

    def textbox(self, bloc_nb):

        textbox = self.textbox

        return textbox



