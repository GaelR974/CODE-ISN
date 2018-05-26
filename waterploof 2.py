import pygame
import time
from random import *
 
pygame.init()
 
 
fenetreL=800
fenetreH=500
taille_Perso=(60,60)
Perso_rect = pygame.Rect((0,0),taille_Perso)
taille_obstacle=(60,60)
obstacle_rect = pygame.Rect((0,0),taille_obstacle)

perso= pygame.display.set_mode(taille_Perso)
obstacle = pygame.display.set_mode(taille_obstacle)
fenetre=pygame.display.set_mode((fenetreL,fenetreH))
 
fond=pygame.image.load("fondjeux.jpg").convert()
fenetre.blit(fond,(0,0))

pygame.display.set_caption("DodgeHead")
horloge = pygame.time.Clock()
 
 
img= pygame.image.load("perso.png")

boule= pygame.image.load("obstacle.png")

Son = pygame.mixer.Sound("chillpiano.wav")
Son.play(loops=-1, maxtime=0, fade_ms=0)



def score(compte):
    police= pygame.font.Font('ButterKings.ttf',20)
    texte =police.render("SCORE:" +str(compte),True,(255,255,255))
    fenetre.blit(texte,[10,0])





def rejoueOUquitte ():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP:
            continue
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
     
    

 
 
#On sauvegarde le volume avant afin de le remettre à l'origine
volume_origin = Son.get_volume()
#Le progamme n'est pas mute au demarage
is_muted=False

while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_m:
                    Son.set_volume(volume_origin)# On est mute ?
                    is_muted=False

                else:

                Son.set_volume(0)#Sinon on mute
                is_muted=True
                print('key m press')
 
   
    
                        
                   
                           
                         
                            
                            
                       

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


    perso_vitesse=1
    score_actuel =0
    horloge.tick(60)
    
    game_over=False
    
    pygame.display.update()
     
    #Valeur a ajuster en fonction du gameplay voulu
    pygame.key.set_repeat(20,10)
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

                 
                    

        fenetre.blit(fond,(0,0))
        y_obstacle +=0.5
        obstacle(x_obstacle,y_obstacle)
        perso(x,y,img)


        score(score_actuel)
            

        

        
        
        
        

        if x>fenetreL-40 or x<-10:
            game0ver()
            
        
        
        pygame.display.update()
 
 
principale()
pygame.quit()
quit()
