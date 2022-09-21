# Exercise 61, checking lists for content

list1 = list(range(2,3,2))
list2 = ["apple", "pear", "orange", "fig", "grape", "banana", "peach"]
list3 = ["flour", "milk", "eggs", "salt", "butter", "sugar", "chocolate"]

check1 = int(input("Enter any even number: "))
while check1 not in list1 :
    check1 = int(input("Enter a smaller even number: "))
else :
    print("Yeah!")
    check2 = input("Enter the name of a fruit I don't know")
    while check2 in list2 :
        check2 = input("I already knew that! Try again: ")
    else:
        print("Good!")
        check3 = input("Guess any ingredient of my favourite cake")
        while check3 not in list3 :
            check3 = input("It's hard, I know. Try again!")
        else:
            print(check3, ", Yes, that was easy!")
