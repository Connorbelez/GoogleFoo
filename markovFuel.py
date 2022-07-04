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
    for i in range(len(g)):
        trans = g[i][:numTransient]

        g[i] = g[i][numTransient:] + trans
    for i in range(len(denoms)):
        if denoms[i] == 1:
            canonM.append(g[i])
    for i in range(len(denoms)):
        if denoms[i] != 1:
            canonM.append(g[i])

    rows = canonM[len(canonM)-numTransient:]
    for element in rows:
        Q.append(element[-numTransient:])


    for element in rows:
        # print(element)
        R.append(element[:len(element) - numTransient])

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

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(list(cofactors))):
        for c in range(len(list(cofactors))):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
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
    #convert the matrix to a proper Markov chain matrix
    M, D = convertToFrac(M)
    #convert the matrix to cannonical form, extract the different quandrants. M = canonicla matrix, R = transient -> terminal prob matrix, TTM transient -> transient matrix
    CM, TTM, TTA = convertToCanonical(M,D)
    I = generateIdentityMatrix(TTM)
    temp = subtractFromIdentity(TTM,I)
    temp = getMatrixInverse(temp)
    SolutionMatrix = matrixMultiplication(temp,TTA)

    # printMatrix(SolutionMatrix)

    terminalProbs,denom = ensureCommonDenom(SolutionMatrix[0])
    terminalProbs.append(denom)

    # print(terminalProbs)
    return terminalProbs


print(solution(g))