# Group Exercise 3, Manipulating lists
# Creating three lists, with 1/2/3 parameters chosen by the user
count1 = int(input("Please enter the desired length of the first list: "))
start2 = int(input("Please enter the startvalue of the second list: "))
end2 = int(input("Please enter the last value of the second list: "))
start3 = int(input("Please enter the startvalue of the third list: "))
end3 = int(input("Please enter the last value of the third list: "))
steps3 = int(input("Please enter the stepsize of the third list: "))

ls1 = list(range(0,count1))
print(ls1, len(ls1))
ls2 = list(range(start2, end2))
print(ls2, len(ls2))
ls3 = list(range(start3,end3,steps3))
print(ls3, len(ls3))
ls_combined = [0,ls1, ls2, ls3]
#print(ls_combined)

# The user decides which list should be manipulated

allowed_manipulation = ["insertion","removal", "reverse", "checking", "index"]
choice = int(input("Which list you want to manipulate? "))
ch_ls = ls_combined.pop(choice)
print(ch_ls)
mani = input("What kind of manipulation (insertion, removal, reverse, checking, index)? ")
while mani not in allowed_manipulation:
    print(mani, "not part of the allowed manipulations")
    mani = input("Please choose out of: \n insertion, removal, reverse, checking, index ")
else:
    if mani == "insertion" :
        ins1 = int(input("What do you want to add? "))
        ind1 = int(input("In which position? "))
        ch_ls.insert(ind1, ins1)
        print("Thank you, this is the new list: \n", ch_ls)
    elif mani == "removal" :
        removal1 = int(input("what item should be removed from the list? " ))
        ch_ls.remove(removal1)
        print("Thank you, this is the new list: \n", ch_ls)
    elif mani == "reverse" :
        ch_ls.reverse()
        print("Thank you, this is the new list: \n", ch_ls)
    elif mani == "checking" :
        check1 = int(input("Enter the item you want to search in the list "))
        if check1 not in list1 :
            print(check1, "is not part of the chosen list")
        else :
            print(check1, "is part of the chosen list")
    elif mani == "index" :
        ind1 = int(input("The index of which item you want to know? "))
        print(ch_ls.index(ind1))
