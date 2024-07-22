def makeStringComposition(string, k):
    kmersList = []

    for i in range(len(string) - k + 1):
        kmersList.append(string[i:i+k])
    
    return sorted(kmersList)

def main():
    inputFileName = '../test/30k_dna_sequel.txt'
    k = int('15')
    outputFileName = '../test/30k_dna_sequel_15mer_composition.txt'

    with open(inputFileName, 'r') as file:
        text = file.readline().strip()

    result = makeStringComposition(text, k)
    
    with open(outputFileName, 'w') as file:
        file.write(','.join(result))

if __name__ == '__main__':
    main()
