# Exercise 14, removing entries
ls1 = ["apple", "banana", "cucumber", "orange"]
ls2 = [1, 3, 6, 11, 13, 17, 19, 23, 29]
ls3 = ["See you!", "Buenos noches", "Hasta la vista!", "Tot ziens!"]
print(ls1, "\n", ls2, "\n", ls3)
# how to refer to elements in a list -> print(ls1[1])

removal1 = input("what item should be removed from list1?")
removal2 = int(input("what item should be removed from list2?"))
removal3 = input("what item should be removed from list3?")

ls1.remove(removal1)
ls2.remove(removal2)
ls3.remove(removal3)
print(ls1, "\n", ls2, "\n", ls3)

#deletion of multiple elements or a slice
del ls2[0:1]
print(ls2)
#or deletion of single elements with pop
print(ls2.pop(3))
print(ls2)
