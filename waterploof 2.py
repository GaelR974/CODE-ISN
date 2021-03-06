import pygame
import time
from random import *
 
pygame.init()
 
 
fenetreL=800
fenetreH=500
taille_Perso=(60,60)

taille_obstacle=(60,60)


perso= pygame.display.set_mode(taille_Perso)
obstacle = pygame.display.set_mode(taille_obstacle)
fenetre=pygame.display.set_mode((fenetreL,fenetreH))
 
fond=pygame.image.load("fondjeux.jpg").convert()
fenetre.blit(fond,(0,0))

pygame.display.set_caption("DodgeHead")
horloge = pygame.time.Clock()
 
 
img= pygame.image.load("perso.png")

boule= pygame.image.load("obstacle.png")
#Assignation des variables pour le son
Son = pygame.mixer.Sound("chillpiano.wav")
Son.play()#lecture du son
SonFin=pygame.mixer.Sound("Son END.wav")
SonPalier=pygame.mixer.Sound("Son palier.wav")

volume_origin = Son.get_volume()
volume_originFin= SonFin.get_volume()


def score(compte):
    police= pygame.font.Font('ButterKings.ttf',20)
    texte =police.render("SCORE:" +str(compte),True,(255,255,255))
    fenetre.blit(texte,[10,0])





def rejoueOUquitte ():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:#Appuie sur un touche pour rejouer
            continue
        Son.play()#L'utilisateur appuie sur la touche et relance la musique
        SonFin.stop()#Stop la musique de la collision
        
        return event.key
    return None
    
    

def creaTexteObj(texte,Police):
    textefenetre=Police.render(texte,True,(255,255,255))
    return textefenetre, textefenetre.get_rect()

def message (texte):
    GROSTexte = pygame.font.Font('ButterKings.ttf' ,150)
    petitTexte = pygame.font.Font('ButterKings.ttf',20)

    GROSTextefen, GROSTexterect = creaTexteObj(texte,GROSTexte)
    GROSTexterect.center = fenetreL/2,  ((fenetreH/2)-50)
    fenetre.blit(GROSTextefen, GROSTexterect)


    petitTextefen, petitTexterect = creaTexteObj("appuyer sur une touche pour continuer",petitTexte)
    petitTexterect.center = fenetreL/2,  ((fenetreH/2)+50)
    fenetre.blit(petitTextefen,petitTexterect)

    pygame.display.update()
    time.sleep(0.5)
    while rejoueOUquitte() == None :
        horloge.tick()
    principale()
        

def game0ver():
    message("BOOM!")
 
def obstacle(x_obstacle,y_obstacle):
    fenetre.blit(boule,(x_obstacle,y_obstacle))
    
def perso(x,y,img):
    fenetre.blit(img,(x,y))

def principale():
    x=365
    y=440
    x_mouvement=0

    x_obstacle=randint(60,740)
    y_obstacle=0
    #Definition pour la vitesse de l'obstacle
    perso_vitesse=1
    obstacle_vitesse=0.7
    obstacle_vitesse_step = 0.15
    score_palier = 10
    score_prochain_palier = 10
    score_actuel =0
    horloge.tick(30)
    
    game_over=False
    is_muted=False 
    pygame.display.update()
     
    #Valeur a ajuster en fonction du gameplay voulu
    pygame.key.set_repeat(70,10)
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
     
            if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_mouvement=-10
                        x+=x_mouvement
                        print('key press <-')
     
                    if event.key == pygame.K_RIGHT:
                        x_mouvement=10
                        x+=x_mouvement
                        print('key press ->')
                    
                    if event.key ==pygame.K_m:
                        if is_muted :
                            Son.set_volume(volume_origin)# On est mute ?
                            is_muted=False
                        else:
                            Son.set_volume(0)#Sinon on mute
                            is_muted=True
                        print('key m press')


        fenetre.blit(fond,(0,0))
        y_obstacle +=obstacle_vitesse
        obstacle(x_obstacle,y_obstacle)
        
        #Obstacle fin
        if y_obstacle > fenetreH - 60 :
            x_obstacle=randint(60,740)
            y_obstacle=0
            score_actuel += 1
            

        # Conflit
        Perso_rect = pygame.Rect((x,y),taille_Perso)
        obstacle_rect = pygame.Rect((x_obstacle,y_obstacle),taille_obstacle)
        

        if obstacle_rect.colliderect(Perso_rect) :
                    print('Conflit')
                    SonFin.play()#lecture du son de la collision
                    print('musique fin')

                    Son.stop()#son principale s'arrete
                
                   
                    print('son muted')


                    game0ver()

        perso(x,y,img)

        if score_prochain_palier == score_actuel:#si c'est egale alors
            score_prochain_palier = score_prochain_palier + score_palier #le palier augmente
            obstacle_vitesse += obstacle_vitesse_step #la vitesse de l'obstacle augmente aussi
            SonPalier.play()#Le son se met à jouer
            
            
            

        score(score_actuel)

        if x>fenetreL-40 or x<-10:
            SonFin.play(loops=0, maxtime=0, fade_ms=0)#le son se met a jouer si il touche les bord

            Son.stop()#le son principale s'arrete
            game0ver()
            
        pygame.display.update()
 
 
principale()
pygame.quit()
quit()
