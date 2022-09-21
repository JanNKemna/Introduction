# group exercise 4 - A big dictionary - not ready yet

amino_acids = {}
amino_acids["Tryptophan"] = {"Abbreviation" : "Trp","Symbol": "W", "Side chains" : "aromatic", "Molar mass": 204.229, "Codons":["UGG"], "essential": "TRUE", "Formula" : {"C":11, "H":12, "N":2, "O":2} }
amino_acids["Leucine"] = {"Abbreviation" :"Leu", "Symbol":"L", "Side chains":"aliphatic", "Molar mass":131.18, "Codons":["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"], "essential": "FALSE", "formula":{"C":6, "H":13, "N":1, "O":2} }
amino_acids["Isoleucine"] = {"Abbreviation" :"Ile", "Symbol":"I", "Side chains":"aliphatic", "Molar mass":131.18, "Codons":["AUU", "AUC", "AUA"], "essential":"FALSE", "formula":{"C":6, "H":13, "N":1, "O":2}}
amino_acids["Valine"] = {"Abbreviation" :"Val", "Symbol":"V", "Side chains":"aliphatic", "Molar mass":117.148, "Codons":["GUU", "GUC", "GUA", "GUG"], "essential":"TRUE", "formula":{"C":5, "H":11, "N":1, "O":2}}
amino_acids["Glycine"] = {"Abbreviation" :"Gly", "Symbol":"G", "Side chains":"aliphatic", "Molar mass":75.067, "Codons":["GGU", "GGC", "GGA", "GGG"], "essential":"FALSE", "formula":{"C":2, "H":5, "N":1, "O":2}}
amino_acids["Proline"] = {"Abbreviation" :"Pro", "Symbol":"P", "Side chains":"aliphatic", "Molar mass":115.132, "Codons":["CCU", "CCC", "CCA", "CCG"], "essential":"FALSE", "formula":{"C":5, "H":9, "N":1, "O":2}}
amino_acids["Alanine"] = {"Abbreviation" :"Ala", "Symbol":"A", "Side chains":"aliphatic", "Molar mass":89.094, "Codons":["GCU", "GCC", "GCA", "GCG"], "essential":"FALSE", "formula":{"C":3, "H":7, "N":1, "O":2}}
print(list(amino_acids.keys()))

# The user can chose between 3 different operations on the collection
mod = input("Would you like to (1) display (2) modify or (3) add an entry? \n ")
if mod == "1" :
    disp1 = input("Which entry should I display\n ")
    print(amino_acids[disp1])

elif mod == "2" :


    print(mod, "was no valid option")
elif mod == "3" :
    print(mod, "was no valid option")

else :
    print(mod, "was no valid option")
