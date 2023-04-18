import DIST_1
import SOL_1

@profile
def prog_dyn(x,y):

    dist = DIST_1.dist_1(x,y)
    align = SOL_1.sol_1(x,y,dist[0])

    #print("distance minimal entre x et y (DIST_1) : "+str(dist[1]))
    #print("alignement optimale entre x et y (SOL_1) : "+str(align))

    return (dist,align)
