with open('../test/100k_dna_sequel.txt', 'r') as file:
    composition = file.readline()

with open('../test/100k_output.txt', 'r') as file:
    expected = file.readline()

def compare(composition, expected):
    wrongCharsCount = 0

    for i in range(len(expected)):
        if composition[i] != expected[i]:
            wrongCharsCount += 1
        
    print(f"\nTotal of {wrongCharsCount} wrong characters out of {len(expected)} characters.\n")
    
compare(composition, expected)
