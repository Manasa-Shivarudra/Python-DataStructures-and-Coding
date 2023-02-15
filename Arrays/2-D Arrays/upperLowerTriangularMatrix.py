## Upper and Lower Triangular Matrix

## space complexity =   O(1)
## Time complexity = O(nxm)

mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def upperTriangle(mat):
    tri = []
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat[0])):
            if i<=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri

tri = upperTriangle(mat)
print(tri)

def lowerTriangle(mat):
    tri = []
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat[0])):
            if i>=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri

lowertri = lowerTriangle(mat)
print(lowertri)