import numpy as np
def find(u, S):
    u_S = S[u]
    while u_S != S[u_S]:
        u_S = S[u_S]
    return u_S

def merge(u, v_S, S):
    u_S = S[u]
    while u_S != S[u_S]:
        aux = S[u_S]
        S[u_S] = v_S
        u_S = aux
    S[u_S] = v_S

def kruskal (V,E):
    E = sorted(E, key = lambda arist: arist[2]) #algoritmo que ordena las aristas (u,v,w) por w
    T = set()
    n= len(V)
    S = list(range(1,n))
    pos = 0
    while T < n-1:
        (u,v,w) = E[pos]
        pos += 1
        u_S = find(u, S) # find is a function that finds the set of S where u is
        v_S = find(v, S)
        if u_S != v_S:
            merge(v, u_S, S)
            T = T.union((u,v,w))
    return T
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
