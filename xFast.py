

class xFast():

    #u is the universe size represented by 2^u -1
    
    class InternalNode():

        def __init__(self, val):

            self.successor = None
            self.predecessor = None

            self.left = None
            self.right = None
            
            self.val = val

    class LeafNode():

        def __init__(self, val, left, right):

            self.left = left
            self.right = right

            self.val = val
    
    def __init__(self, u):


        self.u = u
        self.layers = [dict() for i in range(u)]

        self.root = self.InternalNode(None)


        """"Testing Binary Values"""

       
    def successor(self, val):

        node = self.longestPrefix(val)



        if type(node) == self.LeafNode:
            return node.right
        
        elif type(node) == self.InternalNode:
            if node.successor != None:
                return node.successor
        
            if node.predecessor != None:
                return node.predecessor.right

        return None

    def predecessor(self, val):

        node = self.longestPrefix(val)

        

        if type(node) == self.LeafNode:
            return node.left
        
        elif type(node) == self.InternalNode:

            #print("Internal Node Val", node.val)
            if  node.predecessor != None:
                return node.predecessor

            if  node.successor != None:
                #print("Successors Left", node.successor.left)
                return node.successor.left
        
        return None



    def longestPrefix(self, val):

        best = 0
        
        bottom = 0
        top = self.u

        level = (bottom + top) // 2
        tmp = 0 << self.u

        s = val >> level


        while bottom < top:
            
            if s in self.layers[level].keys():
                best = level
                top = level
            
            else:

                bottom = level + 1

            level = (bottom + top) // 2
            s = val >> level


        if best == 0:
            return None

        print("Found {} on layer {}".format(val, best))
        return self.layers[best][s]   


    def insert(self, val):

        #Value already exists
        if val in self.layers[0]:
            return

        lS = self.successor(val)
        lP = self.predecessor(val)
        lnode = self.LeafNode(val, lP, lS)

        print("Inserting Node With Value {}".format(lnode.val))

        if lP != None:
            print("Predecessor", lP.val)
            lP.right = lnode
            
        if lS != None:
            print("Successor", lS.val)
            lS.left = lnode

        #print(node.left)
        node = lnode
        self.layers[0][val] = node
        

        bits = [1 if digit=='1' else 0 for digit in bin(val)[2:]]

        extend = [0 for i in range(self.u - len(bits))]
        
        bits = extend + bits

        
        
        for i in range(self.u - 1):
            b = val >> i + 1
            
            if b not in self.layers[i+1].keys():
                
                tmpNode = self.InternalNode(b)

                
                if bits[self.u - 1 -i] == 0:
                    tmpNode.predecessor = lnode
                    tmpNode.successor = lnode.right
                    tmpNode.left = node
                
                if bits[self.u - 1 -i] == 1:
                    tmpNode.successor = lnode
                    tmpNode.predecessor = lnode.left
                    tmpNode.right = node

                self.layers[i+1][b] = tmpNode

                node = tmpNode
            
            #Node exists
            else:
                tmpNode = self.layers[i+1][b]

                if bits[self.u - 1 -i] == 0:
                    tmpNode.left = node
                    tmpNode.predecessor = tmpNode.left.successor
                
                if bits[self.u - 1 -i] == 1:
                    tmpNode.right = node
                    tmpNode.successor = tmpNode.right.predecessor

                

        
    def print(self):

        for hashes in self.layers:
            print(hashes.keys())

    
        

x = xFast(4)

x.insert(13)
x.insert(15)
x.insert(8)
x.insert(7)
