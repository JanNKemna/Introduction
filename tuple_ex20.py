# Exercise 20 - Working with tuples
lentpl1 = int(input("Enter the length of the first tuple"))
tpl1 = tuple(range(lentpl1))
lentpl2 = int(input("Enter the length of the second tuple"))
tpl2 = tuple(range(lentpl2))
lentpl3 = int(input("Enter the length of the third tuple"))
tpl3 = tuple(range(lentpl3))
lentpl4 = int(input("Enter the length of the last tuple"))
tpl4 = tuple(range(lentpl4))

print(tpl1, "\n",tpl2, "\n",tpl3, "\n",tpl4)

disp1 = int (input("Which entry do you want to have displayed from tuple1"))
print(tpl1[disp1])
disp2 = int (input("Which entry do you want to have displayed from tuple2"))
print(tpl2[disp2])
disp3 = int (input("Which entry do you want to have displayed from tuple3"))
print(tpl3[disp3])
disp4 = int (input("Which entry do you want to have displayed from tuple4"))
print(tpl4[disp4])

tplfibo = (0,1,1,2,3,5,8,13,21,34,55,89)
print(tplfibo)
