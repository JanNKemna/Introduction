#Exercise 24 - while loops
ls1 = list(range(2,34,3))
print(ls1)

i=0
search = int(input("The index of which number do you need?\n\n"))
while ls1[i] != search :
    i += 1
else :
    print(f"The index of {search} is {i}")

ls2 = list(range(3,48,4))
print(ls2)
print(len(ls2))
i = 0
prod = 1
while i < len(ls2) :
    prod *= ls2[i]
    i += 1
else :
    print(prod)

ls3 = ["Halle", "Halen", "Hallo", "Halensee", "Hallodri"]
i = 0
while i < len(ls3) :
    print(ls3[i])
    i += 1
