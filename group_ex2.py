#Group Exercise Nr 2

nr1 = float(input("Hello Random number generator!\ I need six numbers from you.\n Please enter number 1: "))
nr2 = float(input("Please number 2: "))
nr3 = float(input("Please number 3: "))
nr4 = float(input("Please number 4: "))
nr5 = float(input("Please number 5: "))
nr6 = float(input("Please number 6: "))

tab1 = [nr1, nr2, nr3, nr4, nr5, nr6]
var1 = int(input(f"I created a list {tab1}. Which element should I use first?"))
var1 = tab1[var1]
print(f"You chose {var1}")
var2 = int(input("and the second element?"))
var2 = tab1[var2]
print(f"You chose {var2}")
op1=int(input("Which operation should I perform? \ntype 1 for addidtion\n 2 for substraction\n 3 for multiplication \n 4 for division\n"))

if op1 == 1:
    print("I can do that. The sum is", var1 + var2)
elif op1 == 2:
    print("I can do that. The difference is", var1 - var2)
elif op1 == 3:
    print("I can do that. The product is", var1 * var2)
elif op1 == 4:
    print("I can do that. The quotient is", var1 / var2)
else :
    print(f"Sorry, {op1} was not an option")
