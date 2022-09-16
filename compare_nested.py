#Exercise 72, branching via if/elif function

print("Try to trick me and use two identical numbers in the following task")
nr1 = int(input("Please enter any number"))
nr2 = int(input("Please enter another number"))
nr3 = int(input("Please enter any number"))
nr4 = int(input("Please enter another number"))

if nr1 == nr2:
    print ("You are lazy, number 1 and 2 are identical")
    if nr3 == nr4:
        print ("Super lazy, number 3 and 4 are also the same")
elif nr1 == nr3:
    print ("Repetitive, number 1 and 3 are the same")
    if nr2 == nr4:
        print("nice try, lazy guy! number 2 and 4 are the same, too")
elif nr1 == nr4 or nr2 == nr3:
    print ("Almost got me! number 1 and number 4 or number 2 and 3 are identical")
else:
    print ("too bad, you failed reading the task")

if nr2==nr4 or nr3==nr4:
    print (".\n.\nOh no, you tricked me! ME!! The most powerful algorithm in the world!! \nFear my wrath! O_O")



# Exercise 7,
#if nr1 > nr2 and nr3 > nr4:
#    print ("Super")
#elif nr1 < nr3 and nr2 < nr4:
#    print ("Super")
#elif nr1 == nr4 or nr2 >= nr3:
#    print ("Super")
#elif nr1 <= nr4 or nr2 == nr3:
#    print ("Super")
#else:
#    print ("too bad")
