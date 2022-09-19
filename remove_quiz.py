# Exercise 14, removing entries
ls1 = ["apple", "banana", "cucumber", "orange"]
ls2 = [1, 3, 6, 11, 13]
ls3 = ["See you!", "Buenos noches", "Hasta la vista!", "Tot ziens!"]
print(ls1)
answere1 = input("Hello user! Which item doesn't fit to the rest?\n")
ls1.remove(answere1)
if answere1 != "cucumber":
    print("Oh no, you lost! There is still a vegetable hidden in ", ls1)
else :
    print("Yes! Now there are only fruits left in ", ls1, "\nNext question: ", ls2)
    answere2 = int(input("Which item doesn't fit to the rest?\n"))
    ls2.remove(answere2)
    if answere2 != 6:
        print("Oh no, you lost! There is still a non prime number hidden in:", ls2)
    else :
        print("Yes! Now there are only prime numbers left: ", ls2,"\nNext question:", ls3)
        answere3 = input("Which item doesn't fit to the rest?\n")
        ls3.remove(answere3)
        if answere3 != "Buenos noches":
            print("Oh no, you lost! The phrases don't mean the same: ", ls3)
        else :
            print("Yes! you are grea! They all mean the same in different languages: ", ls3 )
