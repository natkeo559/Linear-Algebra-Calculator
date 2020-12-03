def eigenvals(mtx):
    e = linalg.eig(mtx)[0]
    return e

def eigenvects(mtx):
    v = [linalg.eig(mtx)[1][:,i] for i in range(len(linalg.eig(mtx)[1]))]
    return v
