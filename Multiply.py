def multiply(mtx_1,mtx_2):
    '''Function to multiply two matrices
       Input consists of a matrix mtx 1
       and another matrix mtx 2. If the 
       two matrices cannot be multiplied
       then the function will return 0.

       Example usage:

       mtx_1 = [[1,3],[-1,2]]
       mtx_2 = [[3],[4]]

       input: print(multiply(mtx_1,mtx_2))
       output: [[15],[5]]'''

    size1 = (len(mtx_1),len(mtx_1[0]))
    size2 = (len(mtx_2),len(mtx_2[0]))

    if size1[1] != size2[0]:
        return 0
    else:
        m = []
        for y in range(size1[0]):
            row = []
            for x in range(size2[1]):
                row.append(0)
            m.append(row)

        for i in range(size1[0]):
            for j in range(size2[1]):
                for k in range(size2[0]):
                    m[i][j] += mtx_1[i][k] * mtx_2[k][j]
        return m