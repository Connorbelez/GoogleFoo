# A: process probability matrix
#     -Check for loops, identify loops
#     -modify probability for each
# B:calc probabilities
# 1) find terminal states
# 2) for each terminal state
#     1: check for zero: look at each transient state, if no path for any transient, append 0
#     2: multiply probabilities for each step in path
#]
from fractions import Fraction


g = [[0, 1, 0, 0, 0, 1],
     [4, 0, 0, 3, 2, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]]

def convertToFrac(g):
    FracMatrix = []
    denoms = []
    counter = 0
    for row in g:
        denom = sum(row)
        denoms.append(denom)
        rowToAdd = [Fraction(val,denom) if val > 0 else val for val in row ]
        if denom == 0:
            rowToAdd[counter] = 1
            denoms[counter] = 1

        FracMatrix.append(rowToAdd)
        counter+=1

    return FracMatrix,denoms

def convertToCanonical(g,denoms):

    canonM = []
    Q = []
    R = []
    numTransient = len(denoms) - denoms.count(1)
    # print(numTransient)


    # printMatrix(R)
    return canonM, Q, R

def printMatrix(g):
    for row in g:
        for val in row:
            print val,
        print

# printMatrix([[1,2,3],[4,5,6]])


def generateIdentityMatrix(g):
    rows = len(g)
    colloumns = len(g[0])
    r = [0]*colloumns
    Q = []
    for i in range(rows):
        row = []
        for j in range(colloumns):
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

# generateIdentityMatrix([[1,2],[3,4]])

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
# printMatrix(convertToCanonical(fm,d))

# def MM(X,Y):
#     G = [[0 for i in range(len(Y[0]))] for j in range(len(X))]
#     for i in range(len(G)): #Rows of X = rows of G
#         for j in range(len(G[0])): #coloumns of G == coloumns of Y
#             for k in range(len(Y)): #rows of Y == coloumns of X, k = (y-row index) and (x-coloumn index) ie this gives us the kth element of teh ith row of x and trhwe
#                 G[i][j] += X[i][k] * Y[k][j]
#
#     return G
#
#
def matrixMultiplication(A,B):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*B)] for X_row in A]




def ensureCommonDenom(l):
    highestDenom = 0
    numerators = []

    for val in l:
        if val.denominator > highestDenom:
            highestDenom = val.denominator

    for val in l:
        if val.denominator < highestDenom:
            factor = highestDenom / val.denominator
            numerators.append(val.numerator*factor)
        else:
            numerators.append(val.numerator)

    return numerators, highestDenom


def solution(M):
    if(len(M)) == 1:
        return [1,1]

    #convert the matrix to a proper Markov chain matrix
    M, D = convertToFrac(M)
    if D[0] == 1:
        return [1]+[0]*(len(D)-1)+[1]
    #convert the matrix to cannonical form, extract the different quandrants. M = canonicla matrix, R = transient -> terminal prob matrix, TTM transient -> transient matrix
    CM, TTM, TTA = convertToCanonical(M,D)
    I = generateIdentityMatrix(TTM)
    temp = subtractFromIdentity(TTM,I)
    temp = inverse(temp)
    SolutionMatrix = matrixMultiplication(temp,TTA)

    # printMatrix(SolutionMatrix)

    terminalProbs,denom = ensureCommonDenom(SolutionMatrix[0])
    terminalProbs.append(denom)

    # print(terminalProbs)
    return terminalProbs


print(solution(g))
print(solution([[1]]))