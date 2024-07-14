from assembler import Assembler

def main():
    inputFileName = input('Enter the input file name: ')

    with open(inputFileName, 'r') as file:
        composition = file.readline().strip()

    asm = Assembler(composition)
    
    print("Adjacency Matrix:")
    print('  ' + ' '.join(node for node in asm.nodesDict))
    for node in asm.nodesDict:
        print(node + ' ' + ' '.join(str(asm.adjacencyMatrix[asm.nodesDict[node]][i]) for i in range(len(asm.nodesDict))))

if __name__ == '__main__':
    main()