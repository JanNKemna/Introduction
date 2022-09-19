# Exercise 9+10, creating lists with the range generator and skipping elements (3 argument input into range())
#examples:
#num1=list(range(16))
#print(num1, len(num1))
#num2=list(range(5,16))
#print(num2, len(num2))
#num3=list(range(0,21,2))
#print(num3, len(num3))

count1 = int(input("Please enter the desired length of the first list: "))
count2 = int(input("Please enter the desired length of the second list: "))
count3 = int(input("Please enter the desired length of the third list: "))
count4 = int(input("Please enter the desired length of the fourth list: "))
start5 = int(input("Please enter the startvalue of the fifth list"))
end5 = int(input("Please enter the last value of the fifth list"))
steps5 = int(input("Please enter the stepsize of the fifth list"))


ls1 = list(range(0,count1))
print(ls1, len(ls1))
ls2 = list(range(0,2*count2,2))
print(ls2, len(ls2))
ls3 = list(range(35,4*count3+35,4))
print(ls3, len(ls3))
ls4 = list(range(-6,-2*count4-6,-2))
print(ls4, len(ls4))
if end5 < start5 :
    end5 = end5-steps5
    ls5 = list(range(start5, end5, -steps5))
else :
    end5 = end5+steps5
    ls5 = list(range(start5, end5, steps5))
print(ls5, len(ls5))
