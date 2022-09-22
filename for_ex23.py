#Exercise 23, for-loops

sum = 0
for i in range(21):
     sum += i
print(sum)

ev_sum = 0
for i in range(0,41,2):
    ev_sum += i
print(ev_sum)

un_sum = 0
for i in range(1,42,2):
    un_sum += i
print(un_sum)

list = list(range(23,48,2))
list2 = list.copy()
for i in range(len(list)) :
    list2[-i-1]=list[i]
print(list2)

list3 = []
for i in range(23,48,2) :
    list3.insert(0, i)
print(list3)
