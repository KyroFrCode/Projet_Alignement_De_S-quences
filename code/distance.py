
#structure contenant les séquences x et y
def Struct_Instance(lignes):

    Sequences = {
        
        "X" : (str.strip(lignes[2])).split(' '),
        "Y" : (str.strip(lignes[3])).split(' '),
    }

    return Sequences


# (liste[char] X,liste[char] Y) -> int dist : Calcule la Distance entre les mots x et y naivement
#@profile
def DIST_NAIF(X,Y):
    return DIST_NAIF_REC(X,Y,0,0,0,100000000)

#(liste[char] X,liste[char] Y, int i, int j, int c, int dist) -> dist : Calcule recursivement la distance des mots x et y naivement
#@profile
def DIST_NAIF_REC(X,Y,i,j,c,dist):

    #cas de base
    if (i == (len(X)-1)) and (j == (len(Y)-1)):
        if(c<dist): dist = c
    #recursivite
    else:

        if((i<(len(X)-1)) and (j<(len(Y)-1))):
            dist = DIST_NAIF_REC(X,Y,i+1,j+1,c+csub(X[i],Y[j]),dist)
        if (i<(len(X)-1)):
            dist = DIST_NAIF_REC(X,Y,i+1,j,c+cdel(),dist)
        if (j<(len(Y)-1)):
            dist = DIST_NAIF_REC(X,Y,i,j+1,c+cins(),dist)
    
    return dist

# void -> int : cout d'une suppression
def cdel():
    return 2
# void -> int : cout d'une insertion
def cins():
    return 2
# void -> int : cout d'une substitution
def csub(a,b):

    if(a==b):
        return 0
    if(( a=='A' and b=='T' ) or ( a =='G' and b =='C' ) or (a=='T' and b=='A') or (a == 'C' and a == 'G')):
        return 3
    else:
        return 4