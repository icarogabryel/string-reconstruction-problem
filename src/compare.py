with open('../test/dna.txt', 'r') as file:
    composition = file.readline()

with open('../test/output.txt', 'r') as file:
    expected = file.readline()

dic = {composition: True}

if dic[expected]:
    print("Correct")
