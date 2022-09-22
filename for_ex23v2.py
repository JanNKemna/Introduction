#Exercise 23 - for loop
list = list(range(2,10,2))
list2 = ["Hello", "Guys"]
for elem in list2 :
    print(elem)

# iterating over Matrices
rows = 3
columns = 2

# creating a matrix with the beforehand defined number of rows and columns
mylist = [[0 for x in range(columns)] for x in range(rows)]
print(mylist)

for i in range(rows) :
    for j in range(columns) :
        mylist[i][j] = "%s,%s"%(i,j)
print(mylist)





mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = []
row = 0
col = 0
for row in range(len(mat1[col][:])) :
    #print(mat1[col][row])
    #mat2.insert(row,mat1[col][row])
    #print(mat2)
    for col in range(len(mat1[:][row])) :
        print(mat1[col][row])
        mat2.insert(mat1[col][row],mat1[col][row])
        print(mat2)
