import pygame
import random
pygame.init()

#creer une classe qui gére la notion d'emplacement
class Emplacement(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image=pygame.image.load('assets/images/pomme_dore.png')
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y

    def set_image(self,image):
        self.image=image

#fonction lancement
def lancement():
    global jetons
    global jetons_gagnes
    # choix hasard avec les probabilités
    hasard=random.choices(fruits,cum_weights=(20,45,85,95,100),k=3)
    fruit_gauche=fruits_dict[hasard[0]]
    fruit_milieu=fruits_dict[hasard[1]]
    fruit_droite=fruits_dict[hasard[2]]

    # changement des images
    emplacement_gauche.set_image(fruit_gauche)
    emplacement_milieu.set_image(fruit_milieu)
    emplacement_droite.set_image(fruit_droite)

    # faire vérification des lots
    if hasard[0]== hasard[1]== hasard[2]:
        jetons_gagnes=fruits_dict_gains[hasard[0]]
        jetons+=jetons_gagnes
        print(f"Une ligne d'orange a été complété ! + {jetons_gagnes} Jetons")

# création de la fenetre
width=800
height=460
screen=pygame.display.set_mode((800,460))
pygame.display.set_caption("Machine à sous")
white=[255,255,255]
screen.fill(white)

#argent du joueur
jetons=1000

#dictionnaire de fruits
image_test=pygame.image.load('assets/images/orange.png')
fruits_dict={
    "cerise":pygame.image.load('assets/images/cerise.png'),
    "ananas":pygame.image.load('assets/images/ananas.png'),
    "orange":pygame.image.load('assets/images/orange.png'),
    "pasteque":pygame.image.load('assets/images/pasteque.png'),
    "pomme_dore":pygame.image.load('assets/images/pomme_dore.png')
}

# liste stockant le nom des fruits
fruits=["ananas","cerise","orange","pasteque","pomme_dore"]

fruits_dict_gains={
    "orange":5,
    "cerise":15,
    "ananas":50,
    "pasteque":150,
    "pomme_dore":10000
}

#chargement des emplacements
height_emplacement=height/2+30
emplacement_x_milieu=width/3+62
emplacement_x_gauche=emplacement_x_milieu-image_test.get_width()-22
emplacement_x_droite=emplacement_x_milieu+image_test.get_width()+20


emplacements=pygame.sprite.Group()
emplacement_gauche=Emplacement(emplacement_x_gauche,height_emplacement)
emplacement_milieu=Emplacement(emplacement_x_milieu,height_emplacement)
emplacement_droite=Emplacement(emplacement_x_droite,height_emplacement)

#rangement des emplacements dans le groupe
emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)

#charger l'image de l'arriere plan
fond=pygame.image.load('assets/images/slot.png')
police=pygame.font.SysFont("comicsansms",30)

#boucle pour maintenir la fenetre pygame en eveil
running=True
while running:
    screen.fill(white)
    screen.blit(fond,(0,0))
    emplacements.draw(screen)

    #afficher son nombre de jetons
    text=police.render(str(jetons)+" jetons",True,(0,0,0))
    screen.blit(text,(10,0))

    pygame.display.flip()
    for event in pygame.event.get():   # verifier si le joueur ferme la fenetre
        if event.type==pygame.QUIT:
            running=False
            quit()
        # verifier si le joueur appuie sur une touche
        if event.type==pygame.KEYDOWN:
            #si la touche est : espace
            if event.key==pygame.K_SPACE and jetons>=5:
                lancement()
                jetons-=5
