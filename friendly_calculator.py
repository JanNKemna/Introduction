#friendly calculator

user_name = input("Hello, what is your name?")
print("Good day "+user_name+", I'm your friendly calculator. Today I'm restricted to divisions, sorry")
number_input1 = input("Please give me your first Number: ")
operator1 = input("Which operation do you want me to do? ")
number_input2 = input("Please give me a second Number: ")

number1 = float(number_input1)
number2 = float(number_input2)
op1 = str(operator1)
operation1 = (number1+op1+number2)


print(str(number_input1)+str(operator1)+str(number_input2)+" equals "+str(operation1))
answer = input(user_name+"is this correct? Yes or No: ")
if answer == "Yes":
    print("Ok, nice")
else: print("Oh, I'm sorry, please repeat the program")
