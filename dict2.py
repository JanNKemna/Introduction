# Create a dictionary

phonebook = {"Ariane":123,"Samu":456,"Thomas":789}
print(phonebook)
print(list(phonebook.keys()))
print(list(phonebook.values()))

phonebook["Ariane"] = {"home":+49345, "mobile":+491575}
print(phonebook["Ariane"])
print(list(phonebook.values()))


dictionary1 = {}
dictionary1["Christoph"] = {"Name": "Knorr", "Age": 35, "Employer": "CQ"}
dictionary1["Gundolf"] = {"Name": "Stoll", "Age": 60, "Employer": "IBW"}
dictionary1["Bennet"] = {"Name": "Wiegert", "Age": 40, "Employer": "SCM"}

print(dictionary1)
print(dictionary1["Bennet"])
print(dictionary1["Bennet"]["Employer"])


dict1 = {}
dict1["amino acid"] = "tryptophan"
dict1["codon"] = "UGG"
dict1["symbol"] = "W"
dict1["molar mass"] = 204.229

print(dict1)
print(list(dict1.keys()))
print(list(dict1.values()))

if "amino acid" in dict1 :
    print("Yes")
else:
    print ("No")

if "tryptophan" in list(dict1.values()) :
    print("Yes")
else:
    print ("No")
