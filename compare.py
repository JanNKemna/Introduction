#Exercise 6, branching via if/elif function

nr1 = int(input("Please enter any number"))
nr2 = int(input("Please enter another number"))
nr3 = int(input("Please enter any number"))
nr4 = int(input("Please enter another number"))

if nr1 == nr2 and nr3 == nr4:
    print ("Super")
elif nr1 == nr3 and nr2 == nr4:
    print ("Super")
elif nr1 == nr4 or nr2 == nr3:
    print ("Super")
else:
    print ("too bad")


# Exercise 7,
if nr1 > nr2 and nr3 > nr4:
    print ("Super")
elif nr1 < nr3 and nr2 < nr4:
    print ("Super")
elif nr1 == nr4 or nr2 >= nr3:
    print ("Super")
elif nr1 <= nr4 or nr2 == nr3:
    print ("Super")
else:
    print ("too bad")
