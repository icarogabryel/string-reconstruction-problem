with open('final/IcaroSilva.txt', 'r') as file:
    composition = file.readline()

with open('final/dna_sequel.txt', 'r') as file:
    expected = file.readline()

def compare(composition, expected):
    wrongCharsCount = 0

    for i in range(len(expected)):
        if composition[i] != expected[i]:
            wrongCharsCount += 1
        
    print(f"\nTotal of {wrongCharsCount} wrong characters out of {len(expected)} characters.\n")
    
compare(composition, expected)
