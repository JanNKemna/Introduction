# Exercise 11, Append and extend

#A = [1,2,3,4]
#B = [5,6,7,8]
#C = [A,B]
#print(C)
#print(A.append(B), A)
#print(B.extend(A), B)

list1 = [1,2,4,5,6,7,9,0]
list2 = [456,234,27567,23899.34,236.1,658]
list3 = ["only", "words", "in", "the list"]
list4 = ["january","february","diary"]
list5 = list(range(35,4*12+35,4))
list6 = list(range(-6,-2*21-6,-2))

print(list1,"\n",list2,"\n",list3,"\n",list4,"\n",list5,"\n",list6,"\n")

list1.append(list3)
print(list1)
list2.append(list4)
print(list2)
list1.extend(list5)
print(list1)
list2.extend(list6)
print(list2)
list2.extend(["extension"])
print(list2)
