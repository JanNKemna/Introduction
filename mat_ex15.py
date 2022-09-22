#Exercise 15 - Matrices

mat1 = [[1,2,3],[1,2,3],[1,2,3]]
print(mat1)
mat2 = [list(range(5)),list(range(5,11))]
print(mat2)
mat3 = [list(range(3))]*4
print(mat3)

mat1[1][0] = 15
mat2[0][3] = 27
mat3[2][2] = 19

print(mat1)
print(mat2)
print(mat3)
