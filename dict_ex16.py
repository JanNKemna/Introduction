# Exercise 16 - Simple dictionary
# Creating a dictionary and adding four keys with one value each
dict1 = {}
dict1["amino acid"] = "tryptophan"
dict1["codon"] = "UGG"
dict1["symbol"] = "W"
dict1["molar mass"] = 204.229

#print the whole dictionary and keys or values alone
print(dict1)
print(list(dict1.keys()))
print(list(dict1.values()))

#user can add entries
addkey = input("Hello user! You can add a new entry to dict1.\n Please enter a key first: ")
addval = input("And the corresponding value: ")
dict1[addkey] = addval
print(dict1)

#user can delete entries
delkey = input("Hello user! You can also delete an entry from dict1.\n Please enter the key: ")
if delkey in dict1 :
    del dict1[delkey]
    print(dict1)
else:
    print(f"Sorry, couldn't find {delkey} in dict1") 
