from numpy import array, delete

def det(mtx):
    d = 0
    x = array(mtx)
    if len(mtx[0]) == 2:
        return (x[0][0] * x[1][1] - x[0][1] * x[1][0])
    else:
        for i in range(len(mtx[0])):
            x = delete(mtx,0,0)
            x = delete(x,i,1)
            d += ((-1) ** i) * mtx[0][i] * det(x)
    return d
