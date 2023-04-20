import SOL_2
import distance
import sys

if(len(sys.argv)==1):
    print("Erreur pas de fichier en argument ou chemin incorrect vers le fichier")
    exit()

file = open(sys.argv[1],"r")
lignes = file.readlines()
dist = distance.Struct_Instance(lignes)
x =''.join(dist["X"])
y=''.join(dist["Y"])
print(SOL_2.sol_2(x,y))
file.close()