adjacencyMatrix = [
   # 1, 2, 3, 4, 5, 6
    [0, 1, 1, 0, 0, 0], # 1
    [0, 1, 0, 2, 0, 0], # 2
    [1, 1, 0, 0, 1, 0], # 3
    [0, 0, 1, 0, 0, 1], # 4
    [0, 0, 0, 0, 0, 1], # 5
    [0, 0, 1, 0, 0, 0]  # 6
]

def isStartNode(nodeIndex):
    inDegree = 0
    outDegree = 0

    for i in range(len(adjacencyMatrix)):
        inDegree += adjacencyMatrix[i][nodeIndex]
        outDegree += adjacencyMatrix[nodeIndex][i]

    return inDegree+1 == outDegree # if the node is a start node, the in-degree should be equal to out-degree + 1

def findStartNode():
    for i in range(len(adjacencyMatrix)):
        if isStartNode(i):
            return i
        
    raise Exception("There is no start node")                  
        
def findEulerianPath(adjacencyMatrix):
    eulerianPath = []
    stack = [findStartNode()]

    while stack:
        top = stack[-1] # get the last element in the stack

        for i in range(len(adjacencyMatrix)): # for each node in the graph
            if adjacencyMatrix[top][i] > 0: # if there is an edge between the top node and i node
                stack.append(i) # add node i to the stack
                adjacencyMatrix[top][i] -= 1 # mark the edge as visited by removing it
                break # break the loop to check the new top node
        else:
            eulerianPath.append(stack.pop()) # if there are no outgoing edges, add the top node to the eulerian path

    return eulerianPath[::-1] # return the eulerian path in reverse order

print(findEulerianPath(adjacencyMatrix)) # Expected output: [0, 1, 2, 1, 3, 4]
