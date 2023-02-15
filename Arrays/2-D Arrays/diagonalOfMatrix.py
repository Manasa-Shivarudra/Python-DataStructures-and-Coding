## Finding the Diagonal of a Matrix

# The diagonal of below matrix is 1,5,9
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n= 2

# Space complexity: O(1)
# Time Complexity: O(nxm)

def diagonalOfMatrixLeft(mat,n):
    diagonal = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                diagonal.append(mat[i][j])
    return diagonal

diagonal = diagonalOfMatrixLeft(mat,n)
print("Diagonal Left:", diagonal)

def diagonalOfMatrixRight(mat,n):
    diagonal = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i+j== len(mat)-1:
                diagonal.append(mat[i][j])
    return diagonal

diagonal = diagonalOfMatrixRight(mat,n)
print("Diagonal Right: ",diagonal)


# Space complexity: O(1)
# Time Complexity: O(n)
def diagonalOfMatrixLeft2(mat,n):
    diagonal = []
    for i in range(len(mat)):
        diagonal.append(mat[i][i])
    return diagonal

diagonal = diagonalOfMatrixLeft2(mat,n)
print("Diagonal Left Optimized:", diagonal)

def diagonalOfMatrixRight2(mat,n):
    diagonal = []
    j= len(mat)-1
    for i in range(len(mat)):
        diagonal.append(mat[i][j])
        j-=1
    return diagonal

diagonal = diagonalOfMatrixRight2(mat,n)
print("Diagonal Right Optimized:", diagonal)

