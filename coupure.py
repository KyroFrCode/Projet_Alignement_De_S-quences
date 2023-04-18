import numpy as np
import distance
import DIST_1
import DIST_2

def coupure(x,y,D):
     
    n = len(x)
    m = len(y)

    I = np.zeros((n,m),dtype=int)
    k=1
    #initialise D avec j*Cins et I
    for j in range(0,m):

        D[0][j]=j*distance.cins()
        I[0][j]=j
    
    D[1][0]=distance.cdel()
    I[1][0] = I[0][0]

    while(k<=n):
        for j in range(1,m):
            #calcule du minimum entre les cases gauche, haute et gauche haut-gauche
            D[1][j]=min(D[1][j-1]+distance.cins(),D[0][j]+distance.cdel(),D[0][j-1]+distance.csub(x[k-1],y[j-1]))

            if(D[1][j]== D[0][j]+distance.cdel()):
                I[1][j]=I[0][j]

            elif(D[1][j]== D[1][j-1]+distance.cins()):
                I[1][j]=I[1][j-1]

            elif(D[1][j]== D[0][j-1]+distance.csub(x[k-1],y[j-1])):
                I[1][j]=I[0][j-1]

        for j in range(0,m):
            D[0][j]=D[1][j]
        if(k>1):
            for j in range(m):
                I[0][j]=I[1][j]
        k+=1
        
        #on supprime la 1er lignes des matrices avec la deuxieme
        I[1][0]=I[0][0]
        D[1][0]=D[0][0]+distance.cdel()

    return I[1][m-1]
