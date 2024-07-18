class Assembler:
    def __init__(self, kMers: str):
        self.kMersList = kMers.split(",")
        self.nodesDict = self.makeNodeDict()
        self.adjacencyMatrix = self.makeAdjacencyMatrix()

    def makeNodeDict(self):
        nodesDict = {}
        index = 0
        
        for kMer in self.kMersList:
            prefix = kMer[:-1]
            suffix = kMer[1:]

            if prefix not in nodesDict:
                nodesDict[prefix] = index
                index += 1
            
            if suffix not in nodesDict:
                nodesDict[suffix] = index
                index += 1

        return nodesDict

    def makeAdjacencyMatrix(self):
        adjacencyMatrix = [[0 for i in range(len(self.nodesDict))] for j in range(len(self.nodesDict))]

        for kMer in self.kMersList:
            prefix = kMer[:-1]
            suffix = kMer[1:]

            adjacencyMatrix[self.nodesDict[prefix]][self.nodesDict[suffix]] += 1

        return adjacencyMatrix


def main():
    inputFileName = input('Enter the input file name: ')

    with open(inputFileName, 'r') as file:
        composition = file.readline().strip() #! Take off the leading and trailing whitespaces

    asm = Assembler(composition)
    
    print("Adjacency Matrix:")
    print('  ' + ' '.join(node for node in asm.nodesDict))
    for node in asm.nodesDict:
        print(node + ' ' + ' '.join(str(asm.adjacencyMatrix[asm.nodesDict[node]][i]) for i in range(len(asm.nodesDict))))


if __name__ == '__main__':
    main()