import distance as dist
import numpy as np

#@profile
def dist_1(x,y):

    n = len(x)+1
    m = len(y)+1
    D = np.zeros((n,m),dtype=int)

    for i in range(n):
        for j in range(m):

            if(i==0 and j==0):
                D[i][j] = 0
            elif(i==0):
                D[i][j] = j*dist.cins()
            elif(j==0):
                D[i][j] = i*dist.cdel()
            else:
                D[i][j] = min(D[i][j-1]+dist.cins(),D[i-1][j]+dist.cdel(),D[i-1][j-1]+dist.csub(x[i-1],y[j-1]))
    
    return (D,D[i][j])