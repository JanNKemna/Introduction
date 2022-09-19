# Exercise 13, advanced slicing
# Generates a list with a user defined length
count1 = int(input("Please enter the desired length of your list: "))
ls1 = list(range(0,count1))
print("I generated a list: ", ls1,"\nwith the length of: ",len(ls1))

sub1 = int(input("Which sublists you want to generate? \nenter the last index of sublist1: "))
sub2 = int(input("enter the startindex of sublist2: "))-1
sub3 = int(input("to create sublist3, enter how many indices you want to skip: "))
sub4 = int(input("to create sublist4, enter how many indices you want to skip: "))
subs = sorted([sub1, sub2, sub3, sub4])
while subs[3] > len(ls1) or subs[0] < -len(ls1):
    print("you entered numbers that extend the length of the lists.\nPlease use smaller numbers")
    sub1 = int(input("Which sublists you want to generate? \nenter the last index of sublist1: "))
    sub2 = int(input("enter the startindex of sublist2: "))-1
    sub3 = int(input("to create sublist3, enter how many indices you want to skip: "))
    sub4 = int(input("to create sublist4, enter how many indices you want to skip: "))
    subs = sorted([sub1, sub2, sub3, sub4])
else :
    print("sublist1: ", ls1[:sub1], "sublist2: ", ls1[sub2:], "sublist3: ", ls1[::sub3],"sublist4: ", ls1[::sub4])
