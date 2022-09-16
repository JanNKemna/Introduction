# handling lists
nr1 = int(input("Please enter any number"))
nr2 = int(input("Please enter another number"))
nr3 = int(input("Please enter any number"))
nr4 = int(input("Please enter another number"))

tab1=[nr1, nr2, nr3, nr4]
tab2=sorted(tab1)
print(tab1)
print(tab2)
if tab2[0] == tab2[1] or tab2[1] == tab2[2] or tab2[2] == tab2[3]:
    print("super, you used ")
else:
    print("bad")
