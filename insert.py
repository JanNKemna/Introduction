# Exercise 62, inserting into list

list1 = list(range(2,12,3))
list2 = sorted(["apple", "pear", "orange", "fig", "grape", "banana", "peach"])
list3 = [0, 1, 2, 3, 5, 13, 21, 34, 55]

#Asking the user to add a value to a desired place in list1/2/3,
#inserting it there and printing the new list1/2/3
print("I lost some numbers, can you help me to fill the gaps\n?", list1)
ins1 = int(input("What do you want to add? "))
ind1 = int(input("In which position? "))
list1.insert(ind1, ins1)
print("Thank you, this is the new list: \n", list1)

print("Do you know some more fruits?\n", list2)
ins2 = (input("Which fruit? "))
ind2 = int(input("Where to insert it? "))
list2.insert(ind2, ins2)
print("Thank you, this is the new list: \n", list2)

print("Can you help me to correct and continue the Fibonacci sequence? \n", list3)
ins3 = int(input("What do you want to add? "))
ind3 = int(input("In which position? "))
list3.insert(ind3, ins3)
print("Thank you, this is the new list: \n", list3)
