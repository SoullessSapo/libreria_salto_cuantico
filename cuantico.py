import numpy as np
def prob(vector,posicion):
    posicion = int(posicion)
    vector = np.array(vector)
    vector = np.real(vector)
    mod = np.linalg.norm(vector)
    pos_vector = vector[posicion]
    pos_vector = int(pos_vector)
    mod = int(mod)
    prob = (pos_vector**2)/(mod**2)
    return prob
def prob_1(vector, vector_1):
    np.array((vector))
    np.array(vector_1)
    r = np.linalg.norm(vector)
    q = np.linalg.norm(vector_1)
    adj = np.matrix.getH(q)
    t = np.dot(r, adj)
    return t
def main():
    x = int(input("1,2"))
    if x ==1:
        m = []
        filas = int(input('digite numero de filas de la matriz'))
        for i in range(filas):
            m.append([])
            valor = input("fila {}:".format(i + 1))
            m[i].append(valor)
        q = input("pos")
        res = prob(m,q)
        print(res)
    if x ==2:
        m = []
        filas = int(input('digite numero de filas de la matriz'))
        for i in range(filas):
            m.append([])
            valor = input("fila {}:".format(i + 1))

            m[i].append(valor)
        r = []
        filas = int(input('digite numero de filas de la matriz'))
        for i in range(filas):
            r.append([])
            valo = input("fila {}:".format(i + 1))

            r[i].append(valo)
        q = input("pos")
        res = prob(m, r)
        print(res)
main()

