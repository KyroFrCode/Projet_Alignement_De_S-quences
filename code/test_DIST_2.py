import DIST_2
import distance
import sys

if(len(sys.argv)==1):
    print("Erreur pas de fichier en argument ou chemin incorrect vers le fichier")
    exit()

file = open(sys.argv[1],"r")
lignes = file.readlines()
dist = distance.Struct_Instance(lignes)
print(DIST_2.dist_2(dist["X"],dist["Y"]))
file.close()