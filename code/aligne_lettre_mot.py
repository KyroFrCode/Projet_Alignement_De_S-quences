import mot_gaps
import numpy as np

#aligne les mots x et y
def aligne_lettre_mot(x,y):

    n=len(x)
    m=len(y)

    u=x[0]

    for i in range (m):

        #On regarde si la lettre x existe dans y
        if(y[i] == u):

            mot = mot_gaps.mot_gaps(i)+u+mot_gaps.mot_gaps(m-i-1)

            return mot


    for i in range (m): 
        #on vérifie les paires compatible entre les lettres x et y
        if((u=='A' and y[i]=='T') or (u=='G' and y[i]=='C')):

            mot = mot_gaps.mot_gaps(i)+u+mot_gaps.mot_gaps(m-i-1)


    mot = mot_gaps.mot_gaps(m)+u

    return mot
