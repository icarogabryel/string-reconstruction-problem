class Assembler:
    def __init__(self, kMers):
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
