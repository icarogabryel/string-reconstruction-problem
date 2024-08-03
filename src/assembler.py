class Assembler:
    def __init__(self, kMers: str):
        self.kMersList: list[str] = kMers.split(",") # Receive a string of k-mers separated by commas
        self.bruijnGraph: dict[str, list] = {} # The incidence list is represented as a dictionary where the key is the prefix and the value is a list of suffixes
        self.eulerianPath: list = [] # The Eulerian path of the graph

    def makeBruijnGraph(self):
        for kMer in self.kMersList:
            prefix = kMer[:-1]
            suffix = kMer[1:]

            if prefix not in self.bruijnGraph: # if the prefix key is not in the dictionary, add it and initiate a list as the value. Else do nothing
                self.bruijnGraph[prefix] = []

            self.bruijnGraph[prefix].append(suffix) # Add the suffix to the list of the prefix key
    
    def findStartNode(self): # Find the start node of the Eulerian path in a semi-eulerian graph
        inDegrees: dict[str, int] = {} # The in-degree of each node
        outDegrees: dict[str, int] = {} # The out-degree of each node
        startNode = '' # The start node of the Eulerian path

        # Calculate the in-degree and out-degree of each node
        for node in self.bruijnGraph:
            if node not in inDegrees:
                inDegrees[node] = 0
            
            outDegrees[node] = len(self.bruijnGraph[node]) # The out-degree of a node is the length of the list of suffixes

            for suffix in self.bruijnGraph[node]:
                if suffix not in inDegrees:
                    inDegrees[suffix] = 0
                    
                inDegrees[suffix] += 1 # The in-degree of a node is the number of times it appears as a suffix

        # Find the start node and end node
        for node in self.bruijnGraph:
            if outDegrees[node] == inDegrees[node] + 1:
                startNode = node
        
        if startNode == '': # If there is no node with out-degree = in-degree + 1
            raise Exception("This graph is not semi-eulerian.")
        
        return startNode
    
    def findEulerianPath(self): # Find using Hierholzer's algorithm
        self.makeBruijnGraph() # Make the Bruijn graph
        stack = [self.findStartNode()] # Initialize the stack with the start node

        while stack:
            top = stack[-1] # get the last element in the stack

            if top not in self.bruijnGraph or len(self.bruijnGraph[top]) == 0: # if the node has no more outgoing edges or it is the end node (not in the graph)
                self.eulerianPath.append(stack.pop()) # add the node to the eulerian path by popping it from the stack and removing it from the graph
            else:
                nextNode = self.bruijnGraph[top].pop(0)
                stack.append(nextNode)
            

        self.eulerianPath = self.eulerianPath[::-1] # return the eulerian path in reverse order
    
    def reconstructString(self):
        self.findEulerianPath()
        reconstructedString = self.eulerianPath[0]

        for node in self.eulerianPath[1:]:
            reconstructedString += node[-1]

        return reconstructedString
