class Assembler:
    def __init__(self, kMers: str):
        self.kMersList = kMers.split(",")
        self.nodesDict = self.makeNodesDict()
        self.adjacencyMatrix = self.makeAdjacencyMatrix()

    def makeNodesDict(self):
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
        adjacencyMatrix = [[0 for _ in range(len(self.nodesDict))] for _ in range(len(self.nodesDict))]

        for kMer in self.kMersList:
            prefix = kMer[:-1]
            suffix = kMer[1:]

            adjacencyMatrix[self.nodesDict[prefix]][self.nodesDict[suffix]] += 1

        return adjacencyMatrix
    
    def isStartNode(self, nodeIndex):
        inDegree = 0
        outDegree = 0

        for i in range(len(self.nodesDict)):
            inDegree += self.adjacencyMatrix[i][nodeIndex] # The sum of the column is the in-degree
            outDegree += self.adjacencyMatrix[nodeIndex][i] # The sum of the row is the out-degree

        return inDegree+1 == outDegree # if the node is a start node, the in-degree + 1 should be equal to out-degree
    
    def findStartNode(self):
        for i in range(len(self.nodesDict)):
            if self.isStartNode(i):
                return i
            
        raise Exception("No start node found.")
    
    def findEulerianPath(self):
        eulerianPath = []
        stack = [self.findStartNode()]

        while stack:
            top = stack[-1] # get the last element in the stack

            for i in range(len(self.nodesDict)): # for each node in the graph
                if self.adjacencyMatrix[top][i] > 0: # if there is an edge between the top node and i node
                    stack.append(i) # add node i to the stack
                    self.adjacencyMatrix[top][i] -= 1 # mark the edge as visited by removing it
                    
                    break # break the loop to check the new top node
            else:
                eulerianPath.append(stack.pop()) # if there are no outgoing edges, add the top node to the eulerian path

        return eulerianPath[::-1] # return the eulerian path in reverse order
    
    def reconstructString(self):
        eulerianPath = self.findEulerianPath()
        reconstructedString = ''

        nodeList = [node for node in self.nodesDict]

        for i in eulerianPath:
            reconstructedString += nodeList[i][0]

        reconstructedString = reconstructedString[:-1] + nodeList[eulerianPath[-1]]

        return reconstructedString     


def main():
    inputFileName = input('Enter the input file name: ')

    with open(inputFileName, 'r') as file:
        composition = file.readline().strip() #! Take off the leading and trailing whitespaces

    asm = Assembler(composition)
    
    print("Adjacency Matrix:")
    print('  ' + ' '.join(node for node in asm.nodesDict))
    
    for node in asm.nodesDict:
        print(node + ' ' + ' '.join(str(asm.adjacencyMatrix[asm.nodesDict[node]][i]) for i in range(len(asm.nodesDict))))

    print('DNA Reconstruction:')
    
    with open('output.txt', 'w') as file:
        file.write(asm.reconstructString())


if __name__ == '__main__':
    main()