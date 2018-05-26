import pygame


fond=(0,150,255)

pygame.init()


surfaceL=800
surfaceH=500
persoL=60
persoH=60


surface=pygame.display.set_mode((surfaceL,surfaceH))
pygame.display.set_caption("DodgeHead")


img= pygame.image.load("perso.png")
Son = pygame.mixer.Sound("chillpiano.wav")
Son.play(loops=-1, maxtime=0, fade_ms=0)
 
#On sauvegarde le volume avant afin de le remettre a lorigine
volume_origin = Son.get_volume()
#Le progamme n'est pas mute au demarage
is_muted=False

def perso(x,y,img):
    surface.blit(img,(x,y))

x=365
y=440
x_mouvement=0

perso_vitesse=1

game_over=False

#Valeur a ajuster en fonction du gameplay voulu
pygame.key.set_repeat(100,40)
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True

        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_mouvement=-10
                    x+=x_mouvement
                    print('key press <-')

                if event.key==pygame.K_RIGHT:
                    x_mouvement=10
                    x+=x_mouvement
                    print('key press ->')

                if event.key == pygame.K_m :
                    # On est mute ?
                    if is_muted:
                        #Si oui , on met le volume a la valeur d'origine
                        Son.set_volume(volume_origin)
                        is_muted=False
                    else:
                        #Sinon on mute
                        Son.set_volume(0)
                        is_muted=True
                    print('key m presse')


    surface.fill(fond)
    perso(x,y,img)


    pygame.display.update()



pygame.quit()
quit()
