with open('../test/30k_dna_sequel.txt', 'r') as file:
    composition = file.readline()

with open('../test/30k_output.txt', 'r') as file:
    expected = file.readline()

def compare(composition, expected):
    if composition == expected:
        return "Passed"
    else:
        return "Failed"
    
print(compare(composition, expected))
