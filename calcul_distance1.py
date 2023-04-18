import distance
import sys
#prend un fichier en argument
if(len(sys.argv)==1):
    print("Erreur pas de fichier en argument ou chemin incorrect vers le fichier")
    exit()

file = open(sys.argv[1],"r")
lignes = file.readlines()
dist = distance.Struct_Instance(lignes)
print("X: "+str(dist["X"])+"\nY: "+str(dist["Y"])+"\ntaille_X: "+str(len(dist["X"]))+"\ntaille_Y: "+str(len(dist["Y"])))
print("distance:"+str(distance.DIST_NAIF(dist["X"],dist["Y"])))
file.close()