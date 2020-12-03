def transpose(mtx_1):
    '''Transpose a matrix'''
    m = [[0 for x in range(len(mtx_1[0]))] for x in range(len(mtx_1[1]))]
    for i in range(len(mtx_1[0])):
        for j in range(len(mtx_1[1])):
            m[j][i] = mtx_1[i][j]
    return m
