import PROG_DYN as prgd
import distance
import sys

if(len(sys.argv)==1):
    print("Erreur pas de fichier en argument ou chemin incorrect vers le fichier")
    exit()

file = open(sys.argv[1],"r")
lignes = file.readlines()
dist = distance.Struct_Instance(lignes)
print(prgd.prog_dyn(dist["X"],dist["Y"]))
file.close()