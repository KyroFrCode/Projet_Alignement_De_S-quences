import time
import SOL_2
import distance
import os
#fichier test pour le temps CPU sur tous les genomes jusqu'à un temps limite atteint
def main():
    
    folderpath = "./Instances_genome/" # dossier contenant les fichiers de couple de sequence de genomes a resoudre
    fichiers = os.listdir(folderpath)
    timefile = open('exectime_SOL_2.txt','w') #ouverture du fichier qui va contenir tous les données de temps resolution. #format fichier -> @taille_x @taille_y @temps @nom_du_fichier
    i = 0
    start_time = 0
    end_time = 0

    #on lit chaque fichier et on calcule le temps necessaire pour calculer la distance naivement par DIST_NAIF
    while(i<len(fichiers) and (end_time-start_time)<100):

        if(os.path.isfile(os.path.join(folderpath,fichiers[i])) and os.path.splitext(fichiers[i])[1] == ".adn"):
        
            fichierO = open(os.path.join(folderpath,fichiers[i]),'r')
            lignes = fichierO.readlines()
            struct_sequences = distance.Struct_Instance(lignes)
            print(fichiers[i])
            x=''.join(struct_sequences["X"])
            y=''.join(struct_sequences["Y"])
            start_time = time.time()
            dist = SOL_2.sol_2(x,y)
            end_time = time.time()

            fichierO.close()
            print(str(end_time-start_time))
            timefile.write(str(len(struct_sequences["X"]))+' '+str(len(struct_sequences["Y"]))+' '+str((end_time-start_time))+' '+str(fichiers[i])+"\n")
        
        i+=1
    
    timefile.close()
    return

main()