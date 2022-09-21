# Group Exercise 3, Manipulating lists
# Creating a list with parameters specified by the user
# The for loop let the user create three lists
for i in range(3)  :
    opt = int(input("Hello, let's create a new list. How many parameters would you like to specify?\n "))
    while opt > 3 or opt < 0 :
        opt = int(input("That was no possible number of parameters. Please enter values 1,2 or 3\n "))
    else:
        if opt == 0 :
            print("Ok, I will create a list by my own then")
            ls1 = list(range(-6,-2*34-6,-2))
        elif opt == 1 :
            len1 = int(input("Ok, then enter the length of your list:\n "))
            ls1 = list(range(len1))
        elif opt == 2:
            start2 = int(input("Ok, then enter the first value of your list:\n "))
            end2 = int(input("And the last value of your list:\n "))+1
            ls1 = list(range(start2, end2))
        elif opt == 3:
            start3 = int(input("Ok, then enter the first value of your list:\n "))
            end3 = int(input("And the last value of your list:\n "))+1
            steps3 = int(input("Please enter the stepsize of your list:\n "))
            ls1 = list(range(start3,end3,steps3))
        print(ls1, "\nThe length of your list is", len(ls1))

# Asking for a manipulation and performind it if it is possible
    allowed_manipulation = ["insertion","removal", "reverse", "checking", "index"]
    ch_ls = ls1
    mani = input("What kind of manipulation (insertion, removal, reverse, checking, index)?\n")
    while mani not in allowed_manipulation:
        print(mani, "not part of the allowed manipulations")
        mani = input("Please choose out of: \n insertion, removal, reverse, checking, index \n")
    else:
        if mani == "insertion" :
            ins1 = int(input("What do you want to add?\n "))
            ind1 = int(input("In which position?\n "))
            ch_ls.insert(ind1, ins1)
            print("Thank you, this is the new list: \n", ch_ls)
        elif mani == "removal" :
            removal1 = int(input("what item should be removed from the list?\n " ))
            ch_ls.remove(removal1)
            print("Thank you, this is the new list: \n", ch_ls)
        elif mani == "reverse" :
            ch_ls.reverse()
            print("Thank you, this is the new list: \n", ch_ls)
        elif mani == "checking" :
            check1 = int(input("Enter the item you want to search in the list\n "))
            if check1 not in ch_ls :
                print(check1, "is not part of the chosen list")
            else :
                print(check1, "is part of the chosen list")
        elif mani == "index" :
            ind1 = int(input("The index of which item you want to know?\n "))
            print(ch_ls.index(ind1))
