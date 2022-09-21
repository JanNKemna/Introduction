# Exercise 18 - Protein collection (a nested dictionary)
# Exercise 19 - Adjusting the collection

# Creating a nested dictionary - each entry has a dictionary of features
prot ={}
prot["XopB"] = {"Submitted names": "Xanthomonas outer protein B", "Length": 613, "Mass(Da)": 65521}
prot["HrpG"] = {"Submitted names": "hrc regulated gene G", "Length": 536, "Mass(Da)": 59041}
prot["Clp"] = {"Submitted names": "CRP-like protein Clp", "Length": 230, "Mass(Da)": 25711}
prot["RpfG"] = {"Submitted names": "Cyclic di-GMP phosphodiesterase response regulator RpfG", "Length": 378, "Mass(Da)": 42173}
print(prot)

# The user can chose between 3 different operations on the collection
mod = input("Would you like to (1) delete (2) change or (3) add an entry? \n ")
if mod == "1" :
    del1 = input("Which entry should be deleted?\n ")
    while del1 not in prot :
        print(del1, "was not found in protein dictionary")
        del1 = input("Which entry should be deleted?\n ")
    else:
        del prot[del1]
        print(prot)
# The user can change only the value of a feature, not the name of the feature
elif mod == "2" :
    mod1 = input("Which entry should be changed?\n ")
    while mod1 not in prot :
        print(mod1, "was not found in protein dictionary")
        mod1 = input("Which entry should be changed?\n ")
    else:
        print(prot[mod1])
        mod2 = input("Which of the features do you want to change?\n")
        while mod2 not in prot[mod1] :
            print(mod2, "is not a changable feature of", mod1)
            mod2 = input("Which feature should be changed?\n ")
        else:
            print(prot[mod1][mod2])
            mod3 = input(f"You want to change {prot[mod1][mod2]} to?\n")
            prot[mod1][mod2] = mod3
            print(prot)
# The user can add a new entry abd is guided to use the same datastructure as the rest of the collection -> entry / feature / value
elif mod == "3" :
    entry1 = input("What is the name of your new entry?\n")
    feature2 = input("Which feature do you want to add?\n")
    value3 = input(f"Which value do you want to add to {entry1} under {feature2}?\n")
    prot[entry1] = {feature2 : value3}
    print(prot)
else :
    print(mod, "was no valid option")
