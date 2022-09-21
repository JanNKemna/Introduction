# Playaround with user input and dynamic variables

n = int(input("Enter the number of tuples you would like to create: "))
a = list(map(int,input("\nEnter the length of the tuples seperated by a space:\n ").strip().split()))[:n]
print("\n List is - ", a)

num_elem = len(a)
for i in range(num_elem) :
    print(a[i])
    tpl"i" = tuple(range(a[i]))
    print(tpl"i")



#for i in range (0,n):
#    globals()[f"x{i}"] = i
#    print(x1)
