#retourne un mot avec k gaps
def mot_gaps(k):

    u=""

    if(k==0):
        return u
    else:
        for j in range(k):
            u=u+"_"
    return u