## Find the transpose of a matrix

## Space complexity: O(nxm)
## Time complexity: O(nxm)

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

def transposeOfMatrix(mat):
    transpose = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            row.append(-1)
        transpose.append(row)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            transpose[i][j] = mat[j][i]
    return transpose

trans = transposeOfMatrix(mat)
print(trans)

## Space complexity: O(1)
## Time complexity: O(nxm)

def transpose2OfMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

trans2 = transpose2OfMatrix(mat)
print(trans2)
