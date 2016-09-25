from tkinter import *  # On importe l'interface graphique tkinter
from random import shuffle # on importe la méthode pour rendre aleatoire les mouvements de l'IA


Fenetre = Tk()  # On ouvre la fenetre grace à tkinter
Fenetre.title("Projet - Morpion")  # Nom de la fenetre
Fenetre.configure(background='black')  # Couleur du fond

def MessageAccueil(texte, Label):
    Label.config(text=texte)
ChampLabel = Label(Fenetre)
ChampLabel.configure(width='40', height='3', relief=FLAT, fg="white", bg="black", bd=9)
ChampLabel.grid(row=0, column=1, padx=45, pady=10)
MessageAccueil(('Bienvenue dans le jeu de Morpion !'),
            ChampLabel)
ChampLabel = Label(Fenetre)
ChampLabel.configure(width='40', height='3', relief=FLAT, fg="white", bg="black", bd=9)
ChampLabel.grid(row=2, column=1, padx=45, pady=10)
MessageAccueil(('Que voulez-vous faire?'),
            ChampLabel)
ChampLabel = Label(Fenetre)
ChampLabel.configure(width='40', height='3', relief=FLAT, fg="grey", bg="black", bd=9)
ChampLabel.grid(row=5, column=1, padx=45, pady=10)
MessageAccueil(('Créé par Iris HANNA & Bastien ROBERT'),
            ChampLabel)

ContreIA = 0
quitter = 0

def JouerContreIAFacile():
    global ContreIA
    ContreIA = 2
    Fenetre.destroy()

def JouerContreIAMid():
    global ContreIA
    ContreIA = 3
    Fenetre.destroy()

def JouerContreIADif():
    global ContreIA
    ContreIA = 1
    Fenetre.destroy()



def Quitter():
    global quitter
    quitter = 1
    Fenetre.destroy()
            
BoutonIAdif = Button(Fenetre)
BoutonIAdif.configure(width='25', height='2', relief=GROOVE, bg="red", text = "Jouer contre l'IA Difficile", command=JouerContreIADif)
BoutonIAdif.grid(row=3, column=2, padx=10, pady=5)
BoutonIAdif.bind("<ButtonPress-1>")

BoutonIAmid = Button(Fenetre)
BoutonIAmid.configure(width='25', height='2', relief=GROOVE, bg="orange", text = "Jouer contre l'IA Moyenne", command=JouerContreIAMid)
BoutonIAmid.grid(row=3, column=1, padx=10, pady=5)
BoutonIAmid.bind("<ButtonPress-1>")

BoutonIAfacile = Button(Fenetre)
BoutonIAfacile.configure(width='25', height='2', relief=GROOVE, bg="green", text = "Jouer contre l'IA Facile", command=JouerContreIAFacile)
BoutonIAfacile.grid(row=3, column=0, padx=10, pady=5)
BoutonIAfacile.bind("<ButtonPress-1>")

BoutonJvsJ = Button(Fenetre)
BoutonJvsJ.configure(width='25', height='2', relief=GROOVE, bg="ivory", text = "Jouer contre un autre joueur", command=Fenetre.destroy)
BoutonJvsJ.grid(row=1, column=1, padx=10, pady=5)
BoutonJvsJ.bind("<ButtonPress-1>")

BoutonQuitter= Button(Fenetre)
BoutonQuitter.configure(width='25', height='2', relief=GROOVE, bg="ivory", text = "Quitter", command=Quitter)
BoutonQuitter.grid(row=4, column=1, padx=10, pady=5)
BoutonQuitter.bind("<ButtonPress-1>")

Fenetre.mainloop()



TableauDeJeu = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]  # On initialise le tableau de jeu
TableauDeParametre = [1, 0, 0, 0]  # On initialise l'ordre de jeu et les scores
Fenetre = Tk()  # On ouvre la fenetre grace à tkinter
Fenetre.title("Projet - Morpion")  # Nom de la fenetre
Fenetre.configure(background='black')  # Couleur du fond

ImageVide = PhotoImage(file="Images\Vide.png")  # Images correspondantes
ImageRond = PhotoImage(file="Images\Rond.png")  #
ImageCroix = PhotoImage(file="Images\Croix.png")  #

if quitter == 1:
    exit()

def Message(texte, Label):  # On définit la fonction pour les messages à afficher
    Label.config(text=texte)


def ChangerdeJoueur(joueur):  # On définit la fonction pour changer de joueur -- Iris
    if joueur == 1:
        joueur = 2
    else:
            joueur = 1
    Message(('Joueur ' + str(joueur) + ' à votre tour !'),
            ChampLabel)  #On affiche un message pour indiquer le changement de joueur
    return joueur


def CoordonneeVersBoutons(col, l):  # On définit les boutons par rapport aux coordonnées en fonction des lignes / cases -- Iris
    if l == 0 and col == 0:
        return Bouton1
    if l == 0 and col == 1:
        return Bouton2
    if l == 0 and col == 2:
        return Bouton3
    if l == 1 and col == 0:
        return Bouton4
    if l == 1 and col == 1:
        return Bouton5
    if l == 1 and col == 2:
        return Bouton6
    if l == 2 and col == 0:
        return Bouton7
    if l == 2 and col == 1:
        return Bouton8
    if l == 2 and col == 2:
        return Bouton9


def JoueurVersIcone(joueur):  # On définit l'image à utiliser en fonction du joueur -- Bastien
    if joueur[0] == 1:
        return ImageCroix
    else:
        return ImageRond


def VerificationMatchnul(tab):  # On définit la fonction en cas de match nul -- Bastien
    matchnul = 0
    compzero = 0

    for i in range(3):
        for j in range(3):
            if tab[i][j] == 0:          #Si on ne peut plus remplir aucune case et si personne n'a gagné
                compzero = compzero + 1

    if compzero == 0:                   #On obtient alors un match nul
        matchnul = 1
    else:
        matchnul = 0                    #Si non, pas de match nul
    return matchnul


def ActiverBouton():                        #On définit la fonction qui active tous les boutons -- Bastien
    Bouton1.configure(state=ACTIVE)
    Bouton2.configure(state=ACTIVE)
    Bouton3.configure(state=ACTIVE)
    Bouton4.configure(state=ACTIVE)
    Bouton5.configure(state=ACTIVE)
    Bouton6.configure(state=ACTIVE)
    Bouton7.configure(state=ACTIVE)
    Bouton8.configure(state=ACTIVE)
    Bouton9.configure(state=ACTIVE)


def DesactiverBouton():                     #On définit la fonction qui désactive tous les boutons -- Bastien
    Bouton1.configure(state=DISABLED)
    Bouton2.configure(state=DISABLED)
    Bouton3.configure(state=DISABLED)
    Bouton4.configure(state=DISABLED)
    Bouton5.configure(state=DISABLED)
    Bouton6.configure(state=DISABLED)
    Bouton7.configure(state=DISABLED)
    Bouton8.configure(state=DISABLED)
    Bouton9.configure(state=DISABLED)


def InitialisationPartie(tab, tabparam):    #On définit la fonction initialisant la partie grille / joueur etc. -- Iris
    for ligne in range(3):
        for colonne in range(3):
            tab[ligne][colonne] = 0

    ActiverBouton()
    InitialisationBouton()
    tabparam[0] = 1  # num du joueur
    Message(('Joueur ' + str(tabparam[0]) + ' à votre tour !'), ChampLabel)


def InitialisationBouton():                     #On définit toutes les cases comme vides grâce à l'image vide -- Iris
    Bouton1.configure(image=ImageVide)
    Bouton2.configure(image=ImageVide)
    Bouton3.configure(image=ImageVide)
    Bouton4.configure(image=ImageVide)
    Bouton5.configure(image=ImageVide)
    Bouton6.configure(image=ImageVide)
    Bouton7.configure(image=ImageVide)
    Bouton8.configure(image=ImageVide)
    Bouton9.configure(image=ImageVide)


def EvenementClicBouton(tab, tabparam, col, l):    #On définit la fonction qui permettera à l'appli de réagir aux inputs -- Iris & Bastien
    BoutonX = CoordonneeVersBoutons(col, l)        #On établit le lien avec les boutons définis précedemment
    if BoutonX.__getitem__('state') != DISABLED:
        if tab[l][col] == 0:        #Si les coordonnées sont libres
            tab[l][col] = tabparam[0]

            BoutonX.configure(image=JoueurVersIcone(tabparam))  #On regarde quelle image utiliser

            if VerificationVictoire(tab) == 1:      #si le joueur 1 a gagné
                Message(('Le joueur ' + str(tabparam[0]) + ' gagne !'), ChampLabel)     #Message informatif
                DesactiverBouton()      #On désactive les boutons


                if tabparam[0] == 1:    #Boucle pour ajouter la victoire du J1 au compteur
                    tabparam[1] = tabparam[1] + 1
                    Message(('Nombre de victoire joueur 1 : ' + str(tabparam[1])), VictoireJoueur1)
                else:
                    tabparam[2] = tabparam[2] + 1 #Sinon et pas match nul, victoire J2
                    Message(('Nombre de victoire Joueur 2 : ' + str(tabparam[2])), VictoireJoueur2)

            elif VerificationMatchnul(tab) == 1:    #On vérifie le match nul
                DesactiverBouton()
                tabparam[3] = tabparam[3] + 1       #On comptabilise la match nul
                Message(('Match Nul'), ChampLabel)  #On informe du match nul
                Message(('Nombre de match nul : ' + str(tabparam[3])), VictoireMatchNul)    #On affiche nb de matchs nul

            else:
                tabparam[0] = ChangerdeJoueur(tabparam[0])

            if ContreIA == 1 and tabparam[0] == 2:
                x, y = IADifficile(tab, tabparam)
                EvenementClicBouton(tab, tabparam, y, x)
            if ContreIA == 2 and tabparam[0] == 2:
                x, y = IAFacile(tab, tabparam)
                EvenementClicBouton(tab, tabparam, y, x)
            if ContreIA == 3 and tabparam[0] == 2:
                x, y = IAMoyenne(tab, tabparam)
                EvenementClicBouton(tab, tabparam, y, x)
        else:
            Message(('Les coordonnées sont déjà prises.\n\rVous pouvez rejouer joueur ' + str(tabparam[0])), ChampLabel)

def VerificationVictoire(tab):          #On définit toutes les possibilités selon lesquelles il y a une victoire -- Iris
    victoire = 0

    if tab[0][0] != 0 and tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2]:
        victoire = 1
    elif tab[0][2] != 0 and tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0]:
        victoire = 1
    elif tab[0][0] != 0 and tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2]:
        victoire = 1
    elif tab[1][0] != 0 and tab[1][0] == tab[1][1] and tab[1][1] == tab[1][2]:
        victoire = 1
    elif tab[2][0] != 0 and tab[2][0] == tab[2][1] and tab[2][1] == tab[2][2]:
        victoire = 1
    elif tab[0][0] != 0 and tab[0][0] == tab[1][0] and tab[1][0] == tab[2][0]:
        victoire = 1
    elif tab[0][1] != 0 and tab[0][1] == tab[1][1] and tab[1][1] == tab[2][1]:
        victoire = 1
    elif tab[0][2] != 0 and tab[0][2] == tab[1][2] and tab[1][2] == tab[2][2]:
        victoire = 1
    return victoire

def IAFacile(tab,tabparam):   #IA qui joue au hasard --
    for i in range(0, 3): # on vérifie si l'IA peut gagner ce tour ci
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = tabparam[0]
                if VerificationVictoire(tab) == 1:
                    tab[i][j] = 0
                    return (i, j)
                tab[i][j] = 0

    moves = [(0, 0), (2, 0), (0, 2), (2, 2), (0, 1), (1, 0), (1, 2), (2, 1), (1, 1)] #On joue aléatoirement
    shuffle(moves)
    for move in moves:
        x, y = move
        if tab[x][y] == 0:
            return (x, y)

def IAMoyenne(tab, tabparam):  #IA qui a tendance à attaquer mais néglige la défense -- Bastien
    for i in range(0, 3):
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = tabparam[0]
                if VerificationVictoire(tab) == 1:
                    tab[i][j] = 0
                    return (i, j)
                tab[i][j] = 0

    for i in range(0, 3): # on tente de créer un mouvement gagnant pour le prochain tour
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = tabparam[0]
                for i2 in range(0, 3):
                    for j2 in range(0, 3):
                        if tab[i2][j2] == 0:
                            tab[i2][j2] = tabparam[0]
                            if VerificationVictoire(tab) == 1:
                                tab[i2][j2] = 0
                                tab[i][j] = 0
                                return (i, j)
                            tab[i2][j2] = 0
                tab[i][j] = 0

    if tab[1][1] == 0: # on tente d'occuper le centre
        return (1, 1)

    moves = [(0, 0), (2, 0), (0, 2), (2, 2)] # on tente d'occuper les diagonales en priorité
    shuffle(moves)
    for move in moves:
        x, y = move
        if tab[x][y] == 0:
            return (x, y)

    moves = [(0, 1), (1, 0), (1, 2), (2, 1)] # sinon on occupe les milieux
    shuffle(moves)
    for move in moves:
        x, y = move
        if tab[x][y] == 0:
            return (x, y)

def IADifficile(tab, tabparam):  #IA qui joue sur la défense et l'attaque
    for i in range(0, 3): # on vérifie si l'IA peut gagner ce tour ci
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = tabparam[0]
                if VerificationVictoire(tab) == 1:
                    tab[i][j] = 0
                    return (i, j)
                tab[i][j] = 0
                
    for i in range(0, 3): # on empêche l'adversaire d'avoir un mouvement gagnant au prochain tour
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = (tabparam[0]%2)+1
                if VerificationVictoire(tab) == 1:
                    tab[i][j] = 0
                    return (i, j)
                tab[i][j] = 0
    for i in range(0, 3): # on tente de créer un mouvement gagnant pour le prochain tour
        for j in range(0, 3):
            if tab[i][j] == 0:
                tab[i][j] = tabparam[0]
                for i2 in range(0, 3):
                    for j2 in range(0, 3):
                        if tab[i2][j2] == 0:
                            tab[i2][j2] = tabparam[0]
                            if VerificationVictoire(tab) == 1:
                                tab[i2][j2] = 0
                                tab[i][j] = 0
                                return (i, j)
                            tab[i2][j2] = 0
                tab[i][j] = 0
    
    if tab[1][1] == 0: # on tente d'occuper le centre
        return (1, 1)
    
    moves = [(0, 0), (2, 0), (0, 2), (2, 2)] # on tente d'occuper les diagonales en priorité
    shuffle(moves)
    for move in moves:
        x, y = move
        if tab[x][y] == 0:
            return (x, y)
                
    moves = [(0, 1), (1, 0), (1, 2), (2, 1)] # sinon on occupe les milieux
    shuffle(moves) 
    for move in moves:
        x, y = move
        if tab[x][y] == 0:
            return (x, y)

#Toutes les lignes suivantes décrivent l'image, les ombres, le bouton à appuyer pour le déclencher,les
#coordonnées qui se comptabilisent et la position des boutons sur lesquels on peut appuyer -- Bastien & Iris


Bouton1 = Button(Fenetre)
Bouton1.configure(image=ImageVide, relief=GROOVE)
Bouton1.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=0, l=0: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton1.grid(row=0, column=1, padx=3, pady=3)

Bouton2 = Button(Fenetre)
Bouton2.configure(image=ImageVide, relief=GROOVE)
Bouton2.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=1, l=0: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton2.grid(row=0, column=2, padx=3, pady=3)

Bouton3 = Button(Fenetre)
Bouton3.configure(image=ImageVide, relief=GROOVE)
Bouton3.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=2, l=0: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton3.grid(row=0, column=3, padx=3, pady=3)

Bouton4 = Button(Fenetre)
Bouton4.configure(image=ImageVide, relief=GROOVE)
Bouton4.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=0, l=1: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton4.grid(row=1, column=1, padx=3, pady=3)

Bouton5 = Button(Fenetre)
Bouton5.configure(image=ImageVide, relief=GROOVE)
Bouton5.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=1, l=1: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton5.grid(row=1, column=2, padx=3, pady=3)

Bouton6 = Button(Fenetre)
Bouton6.configure(image=ImageVide, relief=GROOVE)
Bouton6.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=2, l=1: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton6.grid(row=1, column=3, padx=3, pady=3)

Bouton7 = Button(Fenetre)
Bouton7.configure(image=ImageVide, relief=GROOVE)
Bouton7.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=0, l=2: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton7.grid(row=2, column=1, padx=3, pady=3)

Bouton8 = Button(Fenetre)
Bouton8.configure(image=ImageVide, relief=GROOVE)
Bouton8.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=1, l=2: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton8.grid(row=2, column=2, padx=3, pady=3)

Bouton9 = Button(Fenetre)
Bouton9.configure(image=ImageVide, relief=GROOVE)
Bouton9.bind("<ButtonPress-1>",
             lambda event, tab=TableauDeJeu, joueur=TableauDeParametre, col=2, l=2: EvenementClicBouton(tab, joueur,
                                                                                                        col, l))
Bouton9.grid(row=2, column=3, padx=3, pady=3)

BoutonRejouer = Button(Fenetre)
BoutonRejouer.configure(width='6', height='3', text='Rejouer', )
BoutonRejouer.grid(row=2, column=0)
BoutonRejouer.bind("<ButtonPress-1>",
                   lambda event, tab=TableauDeJeu, tabparam=TableauDeParametre: InitialisationPartie(tab, tabparam))



#Les lignes suivantes décrivent la taille, la couleur, les ombres, la position des messages interactifs -- Iris & Bastien


ChampLabel = Label(Fenetre)
ChampLabel.configure(width='30', height='5', relief=GROOVE, bg="beige", bd=9)
ChampLabel.grid(row=1, column=0, padx=25, pady=0)
Message(('Joueur ' + str(TableauDeParametre[0]) + ' à votre tour !'), ChampLabel)

VictoireJoueur1 = Label(Fenetre)
VictoireJoueur1.configure(width='30', height='5', relief=GROOVE, bg="beige", bd=3)
VictoireJoueur1.grid(row=0, column=4, padx=25, pady=0)
Message(('Victoire(s) du joueur 1 : ' + str(TableauDeParametre[1])), VictoireJoueur1)

VictoireJoueur2 = Label(Fenetre)
VictoireJoueur2.configure(width='30', height='5', relief=GROOVE, bg="beige", bd=3)
VictoireJoueur2.grid(row=1, column=4, padx=25, pady=0)
Message(('Victoire(s) du joueur 2 : ' + str(TableauDeParametre[2])), VictoireJoueur2)


VictoireMatchNul = Label(Fenetre)
VictoireMatchNul.configure(width='30', height='5', relief=GROOVE, bg="beige", bd=3)
VictoireMatchNul.grid(row=2, column=4, padx=25, pady=0)
Message(('Nombre de match nul : ' + str(TableauDeParametre[3])), VictoireMatchNul)


Fenetre.mainloop()
