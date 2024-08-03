from assembler import Assembler


def main():
    inputFileName = input('Enter the input file name: ')
    outputFileName = input('Enter the output file name: ')
    
    with open(inputFileName, 'r') as file:
        composition = file.readline()

    asm = Assembler(composition)
    
    with open(outputFileName, 'w') as file:
        file.write(asm.reconstructString())


if __name__ == '__main__':
    main()