import distance
import os

def main():
    
    
    folderpath = "./Instances_genome_test/" # dossier contenant les fichiers de couple de sequence de genomes a resoudre
    fichiers = os.listdir(folderpath)
    i = 0

    while(i<len(fichiers)):

        if(os.path.isfile(os.path.join(folderpath,fichiers[i])) and os.path.splitext(fichiers[i])[1] == ".adn"):
        
            fichierO = open(os.path.join(folderpath,fichiers[i]),'r')
            lignes = fichierO.readlines()
            struct_sequences = distance.Struct_Instance(lignes)
            print(fichiers[i])
            print(distance.DIST_NAIF(struct_sequences["X"],struct_sequences["Y"]))
            fichierO.close()
        
        i+=1
    
    return

main()