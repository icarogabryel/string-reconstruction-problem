def makeStringComposition(string, k):
    kmersList = []

    for i in range(len(string) - k + 1):
        kmersList.append(string[i:i+k])
    
    return sorted(kmersList)

def main():
    inputFileName = input('Enter the file name tha contains a character string: ')
    k = int(input('Enter the value of k: '))
    outputFileName = input('Enter the output file name: ')

    with open(inputFileName, 'r') as file:
        text = file.readline().strip()

    result = makeStringComposition(text, k)
    
    with open(outputFileName, 'w') as file:
        file.write(','.join(result))

    print(f'The result has been saved in {outputFileName}')

if __name__ == '__main__':
    main()
