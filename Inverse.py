def inverse(mtx_1):
    #if det(mtx_1)==0:
    if False:
        print("Matrix is not invertible")
    else:
        eps = 1.0/(10**10)
        identity_mtx = [[0 for x in range(len(mtx_1[0]))] for x in range(len(mtx_1))]

        for i in range(len(mtx_1)):
                identity_mtx[i][i] = 1

        m_tup = mtx_1

        (h, w) = (len(m_tup), len(m_tup[0]))
        for y in range(0,h):
            maxrow = y

            for y2 in range(y+1, h):    # Find max pivot
                if abs(m_tup[y2][y]) > abs(m_tup[maxrow][y]):
                    maxrow = y2

            m = [list(item) for item in m_tup]
            temp = m[y]
            m[y] = m[maxrow]
            m[maxrow] = temp
            #(m[y], m[maxrow]) = (m[maxrow], m[y])
            temp = identity_mtx[y]
            identity_mtx[y] = identity_mtx[maxrow]
            identity_mtx[maxrow] = temp
            #(identity_mtx[y], identity_mtx[maxrow]) = (identity_mtx[maxrow], identity_mtx[y])

            if abs(m[y][y]) <= eps:     # Singular?
                return False

            for y2 in range(y+1, h):    # Eliminate column y
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
                    identity_mtx[y2][x] -= identity_mtx[y][x] * c

        for y in range(h-1, 0-1, -1): # Backsubstitute
            c  = m[y][y]
            for y2 in range(0,y):
                for x in range(w-1, y-1, -1):
                    m[y2][x] -=  m[y][x] * m[y2][y] / c
                    identity_mtx[y2][x] -= identity_mtx[y][x] * identity_mtx[y2][y] / c
            m[y][y] /= c
            identity_mtx[y][y] /= c

            for x in range(h, w):       # Normalize row y
                m[y][x] /= c
                identity_mtx[y][x] /= c

    return identity_mtx
