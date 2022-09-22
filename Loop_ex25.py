#Exercise 25 - Loop through a matrix

# set dimensions of the matrix
rows = 4
columns = 5

# creating a matrix with the beforehand defined number of rows and columns
mymat1 = [[0 for x in range(columns)] for x in range(rows)]
# iterating over Matrices to set new values to the matrix
for i in range(rows) :
    for j in range(columns) :
        mymat1[i][j] = (i+j)**2
print("This is mymat1: ",mymat1)

# iterating through the matrix and looking for the maximum value and it's coordinates
max = 0
val = 0
co = [[0],[0]]
#print(co[0])
#print(co[0][0])
for i in range(rows) :
    for j in range(columns) :
        val = mymat1[i][j]
        if val > max :
            max = val
            co[0][0] = i
            co[1][0] = j
print(f"The largest value inside mymat1 is {max} at position {co}")

#Creating another Matrix with help of list(range()) function
mymat2 = [list(range(12,18)), list(range(13,19)), list(range(2,8))]
print("This is mymat2: ",mymat2)
#print(mymat2[2][2])

max = 0
val = 0
co = [[0],[0]]
#print(co[0])
#print(co[0][0])
for i in range(len(mymat2)) :
    for j in range(len(mymat2[0])) :
        val = mymat2[i][j]
        if val > max :
            max = val
            co[0][0] = i
            co[1][0] = j
print(f"The largest value inside the matrix2 is {max} at position {co}")


# sum up all entries of the matrix
sum = 0
for i in range(len(mymat2)) :
    for j in range(len(mymat2[0])) :
        sum += mymat2[i][j]
print(sum)

# multiplication of each element of matrix1 with each element of matrix2

mymat3 = [list(range(0,3)), list(range(3,6)), list(range(6,9))]
mymat4 = [list(range(0,3)), list(range(3,6)), list(range(6,9))]
print("mymat3: ",mymat3)
print("mymat4: ",mymat4)
# mymat5 = mymat3*mymat4 -> can't multiply sequence by non-int of type "list"
#print(mymat5)
row3 = len(mymat3[:][0])
col4 = len(mymat4[0])
# the resulting matrix has as many rows as the first matrix and as many colums as the second
# a 2x3 matrix * 3*2 matrix would deliver a 2x2 matrix; 3x2*2x3 would  deliver 3x3
mymat5 = [[0 for x in range(col4)] for x in range(row3)]
multisum = 0
#print(mymat5)

# The "i"-loop iterates over the rows of the resulting matrix
for i in range(row3) :
    for j in range(len(mymat3[:][0])) :
        for k in range(len(mymat4[0])) :
            # the value of mymat(i,j) is the sum of of the products of mymat3(i,k)*mymat4(k,j)
            # e.g. first row of matrix1 is elementwise multiplied with first column of matrix 2
            # thus first round of j, first run of k : m1(0,0)*m2(0,0) + second run m1(0,1)*m2(1,0) + third run m1(0,2)*m2(2,0)
            # then k reaches the end,resulting matrix coordinate (i,j) is the sum of first round of j and j goes to next round
            # second round of j : first run of k : m1(0,0)*m2(0,1)+ second run m1(0,1)*m2(1,1) + third rund m1(0,2)*m2(2,1)
            multisum = multisum + mymat3[i][k]*mymat4[k][j]
            #print(f"multisum for step {i}, {j}, {k}, {multisum}")
        mymat5[i][j] = multisum
        multisum = 0
print("The multiplication of mymat3 and mymat4 delivers", mymat5)
