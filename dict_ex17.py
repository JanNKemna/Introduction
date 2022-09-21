# Exercise 17 - searching in dictionaries
# Generating a dictionary named amino_acids containing 11 entries

amino_acids = {}
amino_acids["Tryptophan"] = "Trp", "W"
amino_acids["Leucine"] = "Leu", "L"
amino_acids["Isoleucine"] = "Ile", "I"
amino_acids["Valine"] = "Val", "V"
amino_acids["Glycine"] = "Gly", "G"
amino_acids["Proline"] = "Pro", "P"
amino_acids["Alanine"] = "Ala", "A"
amino_acids["Asparagine"] = "Asn", "N"
amino_acids["Serine"] = "Ser", "S"
amino_acids["Threonine"] = "Thr", "T"
amino_acids["Glutamine"] = "Gln", "Q"
print(amino_acids)

# Asking the user for additional entries
length = len(amino_acids)
amino = dict.copy(amino_acids)
while length < 13 :
    add = input("Hello user! Do you want to work on the amino_acids dictionary? \n Type no to quit \n ")
    while add != "no" :
        addkey = input("Please enter the name of the amino acid you look for: ")
        if addkey not in amino_acids :
            print(f"{addkey} was not in the dictionary yes")
            amino_acids[addkey] = ""
            length = len(amino_acids)
        else :
            print(f"{addkey} is already in the dictionary.\n {amino_acids[addkey]}")
            up1 = input( "Do you want to give additional information?\n")
            while up1 == "Yes" :
                upval = input("Which information? ")
                amino_acids[addkey] = upval
                length = len(amino_acids)
            else :
                print("Ok, you don't want to add anything")
                length = len(amino_acids)
    else :
        if amino == amino_acids :
            print("There where no changes to the dictionary \n", amino)

        else :
            print("This is the old dictionary: \n", amino)
            print("This is the updated dictionary: \n", amino_acids)
        exit()
else :
    print("This is the old dictionary: \n", amino)
    print("This is the updated dictionary: \n", amino_acids)
