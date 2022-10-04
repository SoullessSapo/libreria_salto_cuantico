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
def prob_varianza(m,vector):
    m = np.array(m)
    r = np.linalg.det(m)
    e = np.size(m)
    c = [[i for i in range(e[0])] for j in range(e[1])]
    for i in range(e[0]):
        for j in range(e[1]):
            c[i][j] = (-1) * (i + j) * r
    for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != c[i][j]:
                    return False
    vector = np.array(vector)
    i = np.identity(e[0])
    w = m *vector
    w = np.transpose(w)
    y = np.dot(w,vector)
    h = m - i*y
    g = h*h
    varianza = np.dot(w,g)
    varianza = np.dot(varianza,vector)
    return varianza
def prob_media(m):
    m = np.array(m)
    q = np.linalg.eigvals(m)
    r = np.linalg.eig(m)
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

