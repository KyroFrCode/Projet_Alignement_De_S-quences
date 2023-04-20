import distance as dist
import numpy as np

#@profile
def dist_2(x,y):

    n = len(x)+1
    m = len(y)+1
    D = np.zeros((2,m),dtype=int) #creation de la matrice
    k = 1
    #initialisation de la matrice D
    for j in range(0,m):
        D[0][j]=j*dist.cins()

    D[1][0] = dist.cdel()
    
    for k in range(1,n):

        for j in range(1,m):
            D[1][j]=min(D[0][j-1]+dist.csub(x[k-1],y[j-1]),D[0][j]+dist.cdel(),D[1][j-1]+dist.cins())
        
        for w in range(0,m):
            D[0][w]=D[1][w]
        #suppression de la 1er ligne du tableau avec la seconde
        D[1][0]=D[0][0]+dist.cdel()
        
    return D[0][m-1]
            


