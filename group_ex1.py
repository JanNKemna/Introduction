# group exercise 1 22-09-15

print("First we will calculate some statistics off 5 random integers")
int1 = int(input("Please give me your first integer: "))
int2 = int(input("And a second one: "))
int3 = int(input("And a third one: "))
int4 = int(input("And a fourth one: "))
int5 = int(input("And a fifth one: "))

#calculating the sum of the five integers
sum1 = int1+int2+int3+int4+int5
print(f"Sum: {sum1}")

#the Average
ave1 = (int1+int2+int3+int4+int5)/5
print(f"Average: {ave1}")

# procuct
pro1 = int1*int2*int3*int4*int5
print(f"product: {pro1}")

# calculating the variant
var1 = (int1-ave1)**2+(int2-ave1)**2+(int3-ave1)**2+(int4-ave1)**2+(int5-ave1)**2
print(f"variant: {var1}")

#calculating the standard deviation
dev1 = var1**0.5
print(f"standard deviation: {dev1}")

# turns int1 to int5 into a list
#list1 = list(int1, int2, int3, int4, int5)
#min1 = min(list1)


# calculates the remaining livetime
birth1 = int(input("Please enter the year when you were born: "))
death1 = int(input("and the age you would like to reach"))
age1 = 2022-birth1
age2 = 2021-birth1
rest_live = death1-age1
print(f"\nOK, I guess you are {age1} or {age2} years old then. \n That means you might have only {rest_live} years to live")

# lets you guess the height of Mt.Everest and comments your guess
height1 = float(input("\nGuess the height of the Mt. Everest in km"))
MtEverest =8.849 -height1
if ((MtEverest >1) or (MtEverest <-1)):
    print(f"\nToo bad, you missed it by {MtEverest}km")
else:
    print(f"\nAlmost correct, you missed it only by {MtEverest}km")

# calculates your annual expense on gas and breaks it down to the monthly and daily costs.
gas_con = float(input("\nHow does energy crisis affects your gas bill?\n Please enter your estimated gas consumption in m³"))
gas_prize = float(input("And the actual gas prize (mine is 16.54 cents/kwh)"))

cost = gas_con*10*gas_prize/100
cost_m = cost//12
cost_d = cost/365
ice_cream = cost_d//1.2
print (f"\nMy gosh, you will have to pay {cost} per year!\n or {cost_m} per month. \n or {cost_d} per day.\n Or as my son would say '{ice_cream} cones of icecream each day'")

# calculates your annual expense on electricity and breaks it down to the monthly and daily costs.
elec_con = float(input("\nHow does energy crisis affects your electricity bill?\n Please enter your estimated electricity consumption in kw/h"))
elec_prize = float(input("And the actual electricity prize (mine is 32.54 cents/kwh)"))

cost2 = elec_con*10*elec_prize/100
cost2_m = cost2//12
cost2_d = cost2/365
raisin_breads = cost2_d//0.9
print (f"\nMy gosh, you will have to pay {cost2} per year!\n or {cost2_m} per month. \n or {cost2_d} per day.\n Or as my son would say '{raisin_breads} raisin breads each day'")





#res1 = num1
#res1 -= num2
#print("substraction: "+str(res1))
#res1 = num1
#res1 /= num2
#print("division: "+str(res1))
#res1 = num1
#res1 *= num2
#print("multiplication: "+str(res1))
