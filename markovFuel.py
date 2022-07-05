from fractions import Fraction, gcd



def generateIdentityMatrix(g):
    Q = []
    for i in range(g):
        row = []
        for j in range(g):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        Q.append(row)
    return Q

def subtractFromIdentity(M,I):
    for i in range(len(M)):
        for j in range(len(M[0])):
            I[i][j] -= M[i][j]

    return I

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def matrixMultiplication(A,B):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*B)] for X_row in A]

def ensureCommonDenom(l):

    #Get GCD of list:
    GCD = 0
    commonDenom = 0
    for i in range(len(l)-1):
        if l[i]:
            tGCD = gcd(l[i].denominator,l[i+1].denominator)
            if tGCD > GCD:
                GCD = tGCD
            tcd = (l[i].denominator * l[i+1].denominator)/GCD
            if tcd > commonDenom:
                commonDenom = tcd
    l = [(i * commonDenom).numerator for i in l]
    l.append(commonDenom)
    return l

def convertToFrac(g):
    FracMatrix = []
    denoms = []
    counter = 0
    for row in g:
        denom = sum(row)
        denoms.append(denom)
        rowToAdd = [Fraction(val, denom) if val > 0 else val for val in row]
        if denom == 0:
            rowToAdd[counter] = 1
            denoms[counter] = 1

        FracMatrix.append(rowToAdd)
        counter += 1

    return FracMatrix, denoms


def stdConv(g):
    absorbing = []
    transient = []
    # print(d)
    # printMatrix(g)
    for i in range(len(g)):
        if sum(g[i]) == 0:
            absorbing.append(i)
        else:
            transient.append(i)
    matrixKey = absorbing + transient
    standardM = []
    for val in matrixKey:
        standardM.append([0] * len(matrixKey))

    for i in range(len(matrixKey)):
        for j in range(len(matrixKey)):
            standardM[i][j] = g[matrixKey[i]][matrixKey[j]]

    return standardM, len(absorbing), len(transient)


def solution(m):

    if sum(m[0]) == 0:
        return [1,1]
    MM, abs, trans = stdConv(m)

    M1, D1 = convertToFrac(MM)
    # print(M1)
    RQ = M1[abs:]
    R = []
    Q = []

    for row in RQ:
        R.append(row[:abs])
        Q.append(row[abs:])
    I = generateIdentityMatrix(trans)
    F = inverse(subtractFromIdentity(Q,I))

    FR = matrixMultiplication(F, R)
    return ensureCommonDenom(FR[0])



g = [[0, 1, 0, 0, 0, 1],
     [4, 0, 0, 3, 2, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]
print(solution(g))