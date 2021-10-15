print("Chargement de Pythion...")

CaseState = [0,0,0,0,0,0,0,0,0]

#Une valeur vide est un 0.
#Le joueur 1 a la valeur 1 assignée.
#Le joueur 2 a la valeur 2 assignée.

#Notez que la case 0 dans le code est comptée comme 1 dans le jeu lui même, pour simplifier le jeu auprès des utilisateurs.

from time import sleep
from random import randint

sleep(3)

Joueur = 1

def Affichage():
    print("-------------")
    print("|",CaseState[0],"|",CaseState[1],"|",CaseState[2],"|")
    print("-------------")
    print("|",CaseState[3],"|",CaseState[4],"|",CaseState[5],"|")
    print("-------------")
    print("|",CaseState[6],"|",CaseState[7],"|",CaseState[8],"|")
    print("-------------")

def VictoireContrôle():
    #Contrôle de la victoire du joueur 1.
    if (CaseState[0]==1 and CaseState[1]==1 and CaseState[2]==1) or (CaseState[3]==1 and CaseState[4]==1 and CaseState[5]==1) or (CaseState[6]==1 and CaseState[7]==1 and CaseState[8]==1) or (CaseState[0]==1 and CaseState[4]==1 and CaseState[8]==1) or (CaseState[2]==1 and CaseState[4]==1 and CaseState[6]==1) or (CaseState[0]==1 and CaseState[3]==1 and CaseState[6]==1) or (CaseState[1]==1 and CaseState[4]==1 and CaseState[7]==1) or (CaseState[2]==1 and CaseState[5]==1 and CaseState[8]==1):
        print("")
        print("Le joueur 1 est victorieux !")
        return 1

    #Contrôle de la victoire du joueur 2.
    if (CaseState[0]==2 and CaseState[1]==2 and CaseState[2]==2) or (CaseState[3]==2 and CaseState[4]==2 and CaseState[5]==2) or (CaseState[6]==2 and CaseState[7]==2 and CaseState[8]==2) or (CaseState[0]==2 and CaseState[4]==2 and CaseState[8]==2) or (CaseState[2]==2 and CaseState[4]==2 and CaseState[6]==2) or (CaseState[0]==2 and CaseState[3]==2 and CaseState[6]==2) or (CaseState[1]==2 and CaseState[4]==2 and CaseState[7]==2) or (CaseState[2]==2 and CaseState[5]==2 and CaseState[8]==2):
        print("")
        print("L'ordinateur est victorieux !")
        return 2
    return 0

def NettoyageGrille(): #Sert à nettoyer la grille.
    global CaseState
    if (CaseState[0]!=0 and CaseState[1]!=0 and CaseState[2]!=0 and CaseState[3]!=0 and CaseState[4]!=0 and CaseState[5]!=0 and CaseState[6]!=0 and CaseState[7]!=0 and CaseState[8]!=0) :
        print("")
        print("Oulé ! Cette grille est sale...")
        print("")
        Affichage()
        sleep(2)

        print("")
        print("Mais heureusement, je peux passer un bon coup de nettoyage pour vous !")
        sleep(1)

        print("")
        print("Un petit coup par ci...")
        CaseState = [0,0,0,0,0,0,0,0,0]
        sleep(1)

        print("")
        print("Un petit coup par là...")
        sleep(2)

        print("")
        print("Un dernier coup encore là...")
        sleep(2)

        print("")
        print("Voilà, tout propre !")

        sleep(3)

        print("Bon allez, reprenez votre partie, et que le meilleur gagne !")
        print("")

        if musicalchoices == True :
            winsound.PlaySound(None, winsound.SND_ALIAS | winsound.SND_ASYNC)
            winsound.PlaySound('vsmusic.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        return [0,0,0,0,0,0,0,0,0]
    return CaseState

def TimeToPlay(Joueur):
    CaseInseree = False
    global CaseState

    while CaseInseree != True :
        print("")

        if Joueur == 1 :
            CaseChoisie = int(input("Joueur 1, veuillez entrer le numéro de la case que vous voulez modifier : "))
        elif Joueur == 2 :
            CaseChoisie = int(randint(1,9))
        CaseChoisie -= 1

        if not CaseChoisie < 0 and not CaseChoisie > 8 :
            if CaseState[CaseChoisie] > 0:
                if Joueur == 1:
                    print("")
                    print("...")
                    sleep(3)
                    print("")
                    print("Le mode triche n'est pas encore programmé. Désolé.")
                    sleep(2)
                    print("")
                    print("Mais vous pouvez quand même réesayer une autre case, je ne suis pas horrible.")
                elif Joueur == 2:
                    sleep(0.1)

                CaseInseree = False
            else:
                CaseState[CaseChoisie] = Joueur
                if Joueur == 2:
                    print("L'ordinateur décide de choisir la case",CaseChoisie+1,".")
                sleep(1)
                print("")
                print("La case",CaseChoisie + 1,"est maintenant un",Joueur,".")
                CaseInseree = True
                sleep(2)
        else :
            print("")
            print("Je n'apprécie pas vos façons de tenter de faire disfonctionne ce programme.")
            sleep(2)
            print("")
            print("Mais vous pouvez quand même réesayer une autre case, je ne suis pas horrible.")

print("Pythion, créé par Jordan, a fini de charger.")

sleep(3)

print("Veuillez noter que les cases sont organisées de cette manière...")
CaseState = [1,2,3,4,5,6,7,8,9]
Affichage()
CaseState = [0,0,0,0,0,0,0,0,0]
print("")
print("Bonne chance !")

#sleep(3)

#Music playback.
musicalchoices = bool(input("Voulez-vous de la musique sous Windows ? Répondez avec False ou True."))
if musicalchoices == True :
    import winsound
    winsound.PlaySound('vsmusic.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

Joueur = 1

while VictoireContrôle() == 0:
    CaseState = NettoyageGrille()
    TimeToPlay(Joueur)
    print("")
    print("Voilà l'état des cases : ")
    print("")
    Affichage()
    if Joueur == 1:
        Joueur = 2
    elif Joueur == 2:
        Joueur = 1
    if musicalchoices == True and CaseState.count(1)+CaseState.count(2) == 5 :
        winsound.PlaySound(None, winsound.SND_ALIAS | winsound.SND_ASYNC)
        winsound.PlaySound('vstighter.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)


if musicalchoices == True :
    winsound.PlaySound(None, winsound.SND_ALIAS | winsound.SND_ASYNC)
    winsound.PlaySound('victory.wav', winsound.SND_FILENAME)