from GaussJordan import gauss_jordan

def rank(mtx_1):
    m_rref = gauss_jordan(mtx_1)
    zerows = 0
    for i in range(0,len(m_rref)):
        found = False
        for j in range(0,len(m_rref[0])):
            if m_rref[i][j]!=0:
                found = True
        if found:
            zerows += 1
    return zerows
