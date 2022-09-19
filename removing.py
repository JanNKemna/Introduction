#Examples how remove works

list1 = list(range(0,40,2))
print(list1)
#removes item with the value "2"
list1.remove(2)
print(list1)
# removes the seventhst element of the list
list1.remove(list1[6])
print(list1)
#will not work, can only remove one item at once
#list1.remove(list1[6:8])
#print(list1)
