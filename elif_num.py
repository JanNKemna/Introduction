# Exerice Nr.5 Comparing two numbers
nr1 = float(input("Please enter any number"))
nr2 = float(input("Please enter another number"))

if nr1+nr2 > 100:
    print ("these are big numbers")
elif nr1+nr2 > 10:
    print ("these are mediocre numbers")
elif nr1+nr2 > 5:
    print ("these are small numbers")
else:
    print ("these are very small numbers")
