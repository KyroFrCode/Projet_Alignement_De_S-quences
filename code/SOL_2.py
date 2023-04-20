import mot_gaps
import DIST_1
import aligne_lettre_mot
import coupure
@profile
def sol_2(x,y):
    
    n=len(x)
    m=len(y)
    #cas de bases lors que longueur de x=1 ou y=0 
    if(n==1):
        return (aligne_lettre_mot.aligne_lettre_mot(x,y),y)
    if(m==1):
        return (x,aligne_lettre_mot.aligne_lettre_mot(y,x))
    if(n==0):
        return (mot_gaps.mot_gaps(m),y)
    if(m==0):
        return (x,mot_gaps.mot_gaps(n))
    #recursivte de l'algorithme créer les sous-appels de taille n/2
    else:

        w = coupure.coupure(x,y,DIST_1.dist_1(x,y)[0])

        u=sol_2(x[:int((n/2))],y[:int(w)])
        v=sol_2(x[int((n/2)):],y[int(w):])

        return (u[0]+v[0],u[1]+v[1])