def add(mtx_1,mtx_2):
    '''Function to add two matrices.'''

    size1 = (len(mtx_1),len(mtx_1[0]))
    size2 = (len(mtx_2),len(mtx_2[0]))

    if size1 != size2:
        return 0
    else:
        m = [[0 for x in range(size2[1])] for x in range(size1[0])]

        for i in range(size1[0]):
            for j in range(size1[1]):
                m[i][j] = mtx_1[i][j] + mtx_2[i][j]
        return m

def sub(mtx_1,mtx_2):
    '''Function to subtract two matrices.'''

    size1 = (len(mtx_1),len(mtx_1[0]))
    size2 = (len(mtx_2),len(mtx_2[0]))

    if size1 != size2:
        return 0
    else:
        m = [[0 for x in range(size2[1])] for x in range(size1[0])]

        for i in range(size1[0]):
            for j in range(size1[1]):
                m[i][j] = mtx_1[i][j] - mtx_2[i][j]
        return m
