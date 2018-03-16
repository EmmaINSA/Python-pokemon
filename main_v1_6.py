
from Variables import *
from Fonctions import *


pygame.init()


pygame.display.set_caption("Main v1_6")
fenetre = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)

textSurface = FONT.render(LOREM_IPSUM, 1, BLACK)
textToggle = False

# map.playMusic()
cells = PKMN_CENTER_CELLS_V2


textboxToggle = False
textbox = Objet("Files/textbox_1.png", TEXTBOX_POS)

loop = 1

# pour action quand touche enfoncée :
# 1er arg : temps à attendre avant de lancer la répétition
# 2e arg : temps entre chaque déplacement
pygame.key.set_repeat(50, 100)

while loop:

    pygame.time.Clock().tick(30)   # 30 FPS


    fenetre.blit(pkmn_center_2.fond, ORIGIN_POS)   # pas blit dawn sur bg sinon superposition
    # /!\ l'offset de la map

    # joelle.afficher()
    fenetre.blit(joelle.sprite, JOELLE_POS)

    if textboxToggle:
        fenetre.blit(textbox.sprite, textbox.pos)
    if textToggle:
        texteAfficher = formatText(LOREM_IPSUM)


        for i in range (len(texteAfficher)):
            for j in range(len(texteAfficher[i])):
                fenetre.blit((FONT.render(texteAfficher[i][j]+" ", 1, BLACK)), (TEXT_POS[0]+sumSize(texteAfficher[i][0:j])[0]+j*5, TEXT_POS[1]+i*20))
                # fenetre.blit(textSurface, TEXT_POS)

    fenetre.blit(dawn.sprite, (dawn.pos[0]*16+PKMN_CENTER_OFFSET[0]-8,
                               (dawn.pos[1]-1)*16+PKMN_CENTER_OFFSET[1])) # dernier blit = le + devant

    # dawn.afficher()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            loop = 0

        if event.type == KEYDOWN:  # simplifier ?

            if event.key == K_DOWN:
                if dawn.direction != DOWN:
                    dawn.turn(DOWN)
                elif dawn.canMoveDown(cells):
                    dawn.move(DOWN)

            elif event.key == K_UP:
                if dawn.direction != UP:
                    dawn.turn(UP)
                elif dawn.canMoveUp(cells):
                    dawn.move(UP)

            elif event.key == K_LEFT:
                if dawn.direction != LEFT:
                    dawn.turn(LEFT)
                elif dawn.canMoveLeft(cells):
                    dawn.move(LEFT)

            elif event.key == K_RIGHT:
                if dawn.direction != RIGHT:
                    dawn.turn(RIGHT)
                elif dawn.canMoveRight(cells):    # out of range quand bord de la map = "M"
                    dawn.move(RIGHT)

            elif event.key == K_KP0:

                # interact

                # textboxToggle = not textboxToggle
                dawn.canmove = False
                # dawn.canmove = not dawn.canmove
                # textToggle = not textToggle

                if not textboxToggle:
                    textboxToggle = True
                    textToggle = True
