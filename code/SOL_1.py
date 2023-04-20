
#@profile
def sol_1(x,y,D):

    i=len(x)
    j=len(y)
    u=""
    v=""

    if(i==0):
        u=j*"_"
        v=y
        return (u,v)
    
    if(j==0):
        u=x
        v=i*"_"
        return(u,v)
    
    while(i>0 and j>0):
        #recupre le minimum des trois cases voisins soit gauche en haut et haut gauche
        minimum = min(D[i-1][j],D[i][j-1],D[i-1][j-1])
        
        if(minimum==D[i-1][j]):

            u= x[i-1]+u
            v= "_"+v
            i-=1

        elif(minimum==D[i][j-1]):

            u= "_"+u
            v= y[j-1]+v
            j-=1

        elif(minimum==D[i-1][j-1]):

            u= x[i-1]+u
            v= y[j-1]+v
            i-=1
            j-=1

    return (u,v)