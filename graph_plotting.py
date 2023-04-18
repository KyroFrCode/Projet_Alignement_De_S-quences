import matplotlib.pyplot as p
import sys

def Graphique(filename,xlabel,ylabel,title):

    file = open(filename,"r") # ouverture du fichier filename

    exectime = file.readlines() #lecture de tous les lignes

    taille_x = [] #tab contenant les tailles des mots de x
    taille_y = [] #tab contenant les tailles des mots de y
    temps = [] #tab contenant les temps d'execution des Instances des fonctions

    for ligne in exectime: # recupere les informations du fichier txt et le met dans les tableaux

        tab = ligne.split(' ')
        taille_x.append(tab[0])
        taille_y.append(tab[1])
        temps.append(tab[2])

    file.close()
    t_liste = [str(i) for i in tuple(zip(taille_x,taille_y))] #liste contenant les tuples (n,m) taille de x et y (pour permettre de realiser un plot)

    #plot du graphe avec en abscisse les couples (n,m) et le temps en ordonnee
    p.plot(t_liste,temps,linewidth=3)
    p.xlabel(xlabel)
    p.ylabel(ylabel)
    p.title(title)
    ax = p.gca()
    ax.set_xticklabels(labels=t_liste,rotation=90)
    p.show()

if(len(sys.argv)==5):
    Graphique(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
if(len(sys.argv)==1):
    print("Erreur pas argument du type fichier texte en entrée!")
elif(len(sys.argv)==2):
    print("Erreur xlabel ylabel titre manquant en argument")
elif(len(sys.argv)==3):
    print("Erreur ylabel titre manquant en argument")
elif(len(sys.argv)==4):
    print("Erreur titre manquant en argument")