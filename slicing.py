#Exercise 12, slicing
#Generates and prints two lists
list1 = list(range(0,40,2))
list2 = list(range(1,41,2))
print("list1:",list1,"length: ",len(list1),"\nlist2: ",list2,"length: ",len(list2))

#Asks the user for one slice of each list and checks that the slice is part of the list
#by comparing with the length of the list. If the user fails, the slices can be redifined until they fit to the lists
sli1 = int(input("Which sublists you want to generate? \nenter the start of sublist1: "))
sli2 = int(input("enter the end of sublist1: "))
sli3 = int(input("enter the start of sublist2: "))
sli4 = int(input("enter the end of sublist2: "))
slices = sorted([sli1, sli2, sli3, sli4])
while slices[3] > len(list1) or slices[3] > len(list2) or slices[0] < -len(list1) or slices[0] < -len(list2): 
    print("you entered numbers that extend the length of the lists.\nPlease use smaller numbers")
    sli1 = int(input("\nenter number1: "))
    sli2 = int(input("enter number2: "))
    sli3 = int(input("enter number3: "))
    sli4 = int(input("enter number4: "))
    slices = sorted([sli1, sli2, sli3, sli4])
else :
    print("sublist1: ", list1[sli1:sli2], "\nsublist2: ", list2[sli3:sli4])
