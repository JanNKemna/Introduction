#variable = a container for a value

first_name = "Jan"
last_name = "Kemna"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
print(type(full_name))

age = 31
age += 1
print("Your age is: "+str(age))
print(type(age))

height = 188.5
print("Your height is: "+str(height)+"cm")
print(type(height))

human = False
print(human)
print(type(human))

child1, age1, height1 = "Milan", 4, 104.8
child2, age2, height2 = "Levin", 1, 77.2
boys = True

print(type(child1))
print(type(age1))
print(type(boys))

if boys:
    pronoun1 = "He "
    pronoun2 = "His "
else:
    pronoun1 = "She "
    pronoun2 = "Her "

print("My first child is "+str(child1)+". "+str(pronoun1)+"is "+str(age1)+" years old. "+pronoun2+" height is "+str(height1))
print("My second child is "+str(child2)+". "+str(pronoun1)+"is "+str(age2)+" year old. "+pronoun2+" height is "+str(height2))
