#Group Exercise Nr 2, Variant with while loop
var1 = float(input("Hello Random number generator!\ I need two numbers from you.\n Please enter number 1: "))
var2 = float(input("Please enter number 2: "))
op1=int(input("Which operation should I perform? \ntype 1 for addidtion\n 2 for substraction\n 3 for multiplication \n 4 for division\n"))

while op1 > 4:
  op1 = int(input(f"Sorry, {op1} was not an option. Please choose option 1 to 4:  "))
  if op1 <= 4:
    break
if op1 == 1:
    print("I can do that. The sum is ", var1 + var2)
elif op1 == 2:
    print("I can do that. The difference is ", var1 - var2)
elif op1 == 3:
    print("I can do that. The product is ", var1 * var2)
elif op1 == 4:
    print("I can do that. The quotient is ", var1 / var2)
