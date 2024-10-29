# Álvaro López Pérez: alvaro.lopez.perez@udc.es
# Luca Grygar Casas: luca.grygarc@udc.es

import numpy as np
import time
import pandas as pd

def to_adjacency_matrix(V, E):
    M = np.zeros((len(V), len(V)), dtype=int)
    for i,j,w in E:
        M[i][j] = w
        M[j][i] = w
    return M

def to_vertices_and_edges(M):
    rows, cols = M.shape
    E = set([])
    V = set([])
    for i in range(rows):
        V.add(i)
        for j in range(i+1, cols):
            E.add((i,j,M[i][j]))
    return (V,E)

def create_graph(n, max_distance=50, adjacency_matrix=False):
    a = np.random.randint(low=1, high=max_distance, size=(n,n))
    M = np.tril(a,-1) + np.tril(a, -1).T
    if adjacency_matrix:
        return M
    return to_vertices_and_edges(M)

def medir_time(algoritmo,random_l, n:int, k= 1000):
    '''
    Mide el tiempo que tarda un algoritmo en ordenar la lista de n elementos
    random_l que puede ser aleatoria, descendente o ascendente.

    Parameters
    ----------
    algoritmo : TYPE
                function
        DESCRIPTION.
        Algoritmo de ordenamiento
    random_l : TYPE
                list
        DESCRIPTION.
        tipo de lista a usar
    n : TYPE
        int
        DESCRIPTION.
        tamaño de la lista
    k : TYPE, optional
        int
        DESCRIPTION. The default is 1000.
        repetición auxiliar si no se supera el umbral

    Returns
    -------
    t : TYPE
        float
        DESCRIPTION.
        tiempo de ejecución
    A : TYPE
        bool
        DESCRIPTION.
        si se necesitó utilizar el agoritmo varias veces = True

    '''
    A = False
    t1 = time.time_ns()
    x = random_l(n)
    algoritmo(x)
    t2 = time.time_ns()
    t = t2-t1
    if t < 500000:
        A = True
        t1 = time.time_ns()
        for i in range(k):
            x = random_l(n)
            algoritmo(x)
        t2 = time.time_ns()
        T1 = t2 - t1
        t1 = time.time_ns()
        for i in range(k):
            x = random_l(n)
        t2 = time.time_ns()
        T2 = t2-t1
        t = (T1-T2)/k
    
    return (t, A)

def convert_n(n:int ,O_case: int, for_str:bool):
    '''
    Usa un código de números para ofrecer una operación con n o una etiqueta

    Parameters
    ----------
    n : int
        DESCRIPTION.
        número de casos
    O_case : int
        DESCRIPTION.
        tipo de operación o etiqueta
    for_str : bool
        DESCRIPTION.
        si es true devuelve la etiqueta

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    if for_str:
        if O_case==1:
            return "n**2"
        if O_case==2:
            return "n*log2(n)"
        if O_case==3:
            return "n**2.2"
        if O_case==4:
            return "n"
        if O_case==5:
            return "log2(n)"
    else:
        if O_case==1:
            return n**2
        if O_case==2:
            return n*np.log2(n)
        if O_case==3:
            return n**2.2
        if O_case==4:
            return n
        if O_case==5:
            return np.log2(n)

def datos(title,algoritmo, random_l,O_min, O_nor, O_max, d = 100, rep = 7, excel = False):
    '''
    Crea un dataframe a partir del algoritmo y el tipo de lista a evaluar,
    las cotas estimadas por el usuario el inicio de la medición, el número 
    de mediciones y la opción de crear un archivo excel con la tabla

    Parameters
    ----------
    title : TYPE
        str
        DESCRIPTION.
        nombre del archivo
    algoritmo : TYPE
                func
        DESCRIPTION.
        función a evaluar
    random_l : TYPE
            list
        DESCRIPTION.
        
    O_min : TYPE
            int
        DESCRIPTION.
    O_nor : TYPE
            int
        DESCRIPTION.
    O_max : TYPE
            int
        DESCRIPTION.
    d : TYPE, optional
    int
        DESCRIPTION. The default is 100.
    rep : TYPE, optional
    int
        DESCRIPTION. The default is 7.
    excel : TYPE, optional
    bool
        DESCRIPTION. The default is False.
        si es true se hace un excel con nombre title

    Returns
    -------
    .xlsx
    
    '''
    data = pd.DataFrame(columns=['n', 'Time(ns)','More_tests?',
                                 "t(n)/O("+convert_n(0,O_min,True)+ ")",
                                 "t(n)/O("+convert_n(0,O_nor,True)+")",
                                 "t(n)/O("+convert_n(0,O_max,True)+")"])
    for i in range(rep):
        n = (2**(i))*d
        (t,A) = medir_time(algoritmo,random_l, n)
        O_min_aux= t/convert_n(n,O_min,False)
        O_nor_aux= t/convert_n(n,O_nor,False)
        O_max_aux= t/convert_n(n,O_max,False)
        data = data.append({"n": n, 'Time(ns)': t, 'More_tests?': A,
                            "t(n)/O("+convert_n(0,O_min,True)+ ")": O_min_aux,
                            "t(n)/O("+convert_n(0,O_nor,True)+")": O_nor_aux,
                            "t(n)/O("+convert_n(0,O_max,True)+")": O_max_aux},
                            ignore_index=True)
    print(data)

    if excel:
        data.to_excel(str(title)+".xlsx", index= False)


if __name__ == "__main__":
    (V, E) = create_graph(20)
    print(to_adjacency_matrix(V, E))