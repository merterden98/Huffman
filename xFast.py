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

        self.root = self.InternalNode("Dummy")


        

       
    def successor(self, val):

        node = self.longestPrefix(val)

        

        if type(node) == self.LeafNode:
            return node.right
        
        elif type(node) == self.InternalNode:

            if node.val == "Dummy":
                if not bool(self.layers[self.u -1]):
                    return None
                
                if 0 in self.layers[self.u - 1].keys() and val >> self.u -1 == 0:
                    return self.layers[self.u -1][0].predecessor

                if 1 in self.layers[self.u - 1].keys() and val >> self.u -1 == 1:
                    return self.layers[self.u - 1][1].successor

            
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

            if node.val == "Dummy":
                if not bool(self.layers[self.u -1]):
                    return None
                
                if 0 in self.layers[self.u - 1].keys() and val >> self.u -1 == 0:
                    
                    return self.layers[self.u -1][0].predecessor

                if 1 in self.layers[self.u - 1].keys() and val >> self.u -1 == 1:
                    return self.layers[self.u - 1][1].predecessor
                
            #print("Internal Node Val", node.val)
            if  node.predecessor != None:
                #print("Successors Left", node.successor.left)
                return node.predecessor

            if  node.successor != None:
                return node.successor.left

            
        
        return None



    def longestPrefix(self, val):


        if val in self.layers[0].keys():
            return self.layers[0][val]
        
        best = 0
        
        bottom = 0
        top = self.u

        level = (bottom + top) // 2
        tmp = 0 << self.u

        s = val >> level


        while bottom < top:
            
            
            if s in self.layers[level].keys():

                if level != 0:
                    best = level
                top = level
                
            
            else:

                bottom = level + 1

            level = (bottom + top) // 2
            s = val >> level


        if best == 0:
            return self.root

  
        return self.layers[best][s]   


    def insert(self, val):

        #Value already exists
        if val in self.layers[0]:
            return

        lS = self.successor(val)
        lP = self.predecessor(val)
        lnode = self.LeafNode(val, lP, lS)


        if lP != None:
            lP.right = lnode
            
        if lS != None:
            lS.left = lnode

        #print(node.left)
        node = self.root
        self.layers[0][val] = lnode
        

        bits = [1 if digit=='1' else 0 for digit in bin(val)[2:]]

        extend = [0 for i in range(self.u - len(bits))]
        
        bits = extend + bits
        
        for i in range(len(bits) - 1):
            #left or left  child exists
            if (node.left != None and bits[i] == 0) or (node.right != None and bits[i] == 1):
                
                if node.successor != None and node.successor == lS:
                    node.successor = lnode

                if node.predecessor != None and node.predecessor == lP:
                    node.predecessor = lnode

                if bits[i] == 0:
                    
                    node = node.left

                else:
                    
                    node = node.right

            else:
                tmpNode = self.InternalNode(val >> self.u - i - 1)

                if bits[i+1] == 1:
                    tmpNode.successor = lnode
                if bits[i+1] == 0:
                    tmpNode.predecessor = lnode

                if bits[i] == 0:
                    node.left = tmpNode
                    node.successor = None

                    if node.predecessor == None and node.right == None:
                        node.predecessor = lnode

                
                
                if bits[i] == 1:
                    node.right = tmpNode
                    node.predecessor = None

                    if node.successor == None and node.left == None:
                        node.successor = lnode
            
                node = tmpNode

                self.layers[self.u - 1 - i][node.val] = node
                

##TODO Implement Delete         
              
    def delete(self, val):

        deletenode = True
        deleted = False

        if val not in self.layers[0].keys():
            return
        
        for i in range(self.u):
            
            node = self.layers[i][val >> i]

            #Leaf Node So Need to reconnect
            if i == 0:
                
                leaf = node
                nodel = node.left
                noder = node.right

                if nodel != None:
                    nodel.right = noder
                
                if noder != None:
                    noder.left = nodel
                
            #Internal Node Case
            else:
                
                #previous node was a 0 child
                if node.left == prevnode:
                    
                    if deleted == True:
                        node.left = None

                        
                    
                        #This node still has a right child
                        if node.right != None:
                            node.successor = noder
                            deletenode = False
                    
                    if node.predecessor == leaf:
                        node.predecessor = nodel

                        

                    #previous node was a 1 child
                if node.right == prevnode: 
                    if deleted == True:
                        
                        node.right = None
                    #This node still has a left child
                        if node.left != None:
                            node.predecessor = nodel
                            deletenode = False

                    if node.successor == leaf:
                        node.successor = noder


            if deletenode == True:
                self.layers[i].pop(val>>i, 'None')
                deleted = True
            
            else:
                deleted = False
                

            
            prevnode = node
            
        
    def print(self):

        for hashes in self.layers:
            print(hashes.keys())

    
        



