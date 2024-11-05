import numpy as np

def prim (M: np.matrix):
    n = len(M[1])
    mindist = np.repeat(0, n)
    nearest = np.repeat(0, n)
    T = set([])

    for i in range(1,n):
        mindist[i] = M[i,0]

    for i in range(n-1):
        min = np.inf
        for j in range(1,n):
            if 0< mindist[j]<min:
                min = mindist[j]
                k = j
        a = (nearest[k],k,M[nearest[k],k])
        T.add(a)
        mindist[k] = 0
        for j in range(1,n):
            if 0<M[j,k]<mindist[j]:
                mindist[j] = M[j,k]
                nearest[j] = k
    return T
