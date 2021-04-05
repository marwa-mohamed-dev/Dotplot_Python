###################################
#          DM2 : Dotplot          # 
###################################

#Introduction DM 2
import time
print("Bienvenue dans notre programme!!!")
time.sleep (1)
print("Celui-ci permettra la création d'un dotplot en fonction des séquences nucléotidiques, de taille inférieure ou égale à 15, de votre choix.")
time.sleep (2)
print("La fenêtre est fixée à w=3. \n Le seuil sera entré par l'utilisateur, vous pourrez choisir un seuil compris entre 1 et 3.")
time.sleep(3)

## Fonction validant la séquence entrée
def valide(sequence) :  
    for base in sequence : # Pour chaque base de la séquence
        if not (base in "ATCGagct") :  # Si la lettre de correspond pas à la liste de lettres données
            print("La séquence suivante :",sequence," n'est pas valide.")# Affichage erreur
            sequence = input("Veillez entrer une séquence correcte : ") # Demande d'entrée une nouvelle séquence
        if(len(sequence)>15) :
            print("La séquence entrée est trop longue.")# Affichage erreur
            sequence = input("Veillez entrer une séquence correcte : ") # Demande d'entrée une nouvelle séquence
    sequence = sequence.upper() # Mettre la séquence en majuscule
    return(sequence) # Retourne la séquence
# ===========================================================================================
## Fonction créant la matrice 
def creationMatrice (nbL, nbC, seq1, seq2) : # nbL : nombre de lignes, nbC : nombre de colonnes
    MAT = [[" "] * (nbC) for _ in range (nbL)] # Création de la matrice
    for j in range(1,nbC) : # Ajout séquence2 sur ligne 0
        MAT[0][j]=seq1[j-1]
    for i in range(1,nbL) : # Ajout séquence1 sur colonne 0
        MAT[i][0]=seq2[i-1]
    comparaison(seq1, seq2, MAT) # Appel de la fonction comparaison
    affichageMatrice(nbL, MAT) # Appel de la fonction affichageMatrice
    return (MAT) # Retourne la matrice
# ===========================================================================================
## Fonction d'ajout et de vérification du seuil
def ajoutSeuil () : 
    seuil = int(input("Valeur seuil : ")) # Initialisation seuil de type int
    if ((seuil<1) or (seuil>3)) : # Si le seuil n'est pas compris entre 1 et 3
        print("seuil non valid. Veuillez reecrire le seuil (1, 2 ou 3)") # Affichage erreur
        seuil = int(input("Valeur seuil : ")) # Redemande du seuil
    else :
        return (seuil) # Retourne le seuil
# =========================================================================================== 
## Fonction comparant les sequences 1 et 2
def comparaison (seq1, seq2, MAT)
    seuil = ajoutSeuil()
    ressemblance=0 # Initialisation ressemblance
    for i in range(0,len(seq1)-2) : # Initialisation de la fenêtre pour la sequence1 
        fenetre1 = seq1[i:i+3]
        for j in range(0,len(seq2)-2) : # Initialisation de la fenêtre pour la sequence2
            fenetre2 = seq2[j:j+3]
            for x in range(0,3) : # Comparaison des deux fenêtres
                if(fenetre1[x]==fenetre2[x]) : # Si mêmes nucléotides 
                    ressemblance += 1 # Incrémentation de ressemblance
            if(ressemblance>=seuil) : # Si ressemblance supérieur ou égal au seuil
                MAT[j+1][i+1]="*"     # Ajout d'une étoile à la position donnée          
            ressemblance = 0 # Réinitialisation de ressemblance 
# ===========================================================================================           
## Fonction affichant la matrice 
def affichageMatrice (nbL, MAT) :
    for j in range(nbL):
        print(MAT[j]) # Affiche matrice ligne par ligne
        
##########################################
#                   main                 #
##########################################

# Déclaration de variables
# Entrée et vérification des séquences
sequence1 = input("Entrer la première séquence : ")
sequence1 = valide(sequence1)
sequence2 = input("Entrer la deuxième séquence : ")
sequence2 = valide(sequence2)
# Initialisation des lignes et des colonnes 
colonnes = len(sequence1)+1
lignes = len(sequence2)+1
# Création du DotPlot
matrice=creationMatrice(lignes,colonnes,sequence1, sequence2)







