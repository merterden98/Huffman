

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

        # self.layers[1][0b010] = self.InternalNode(0b101)

        # self.layers[2][0b00] = self.InternalNode(0b00)
        # self.layers[2][0b01] = self.InternalNode(0b01)
        # self.layers[2][0b10] = self.InternalNode(0b10)
        # self.layers[2][0b11] = self.InternalNode(0b11)

        # self.layers[3][0b0] = self.InternalNode(0b0)
        # self.layers[3][0b1] = self.InternalNode(0b1)
        
    def successor(self, val):

        node = self.longestPrefix(val)



        if type(node) == self.LeafNode:
            return node.right
        
        else:
            if node.successor != None:
                return node.successor
        
            if node.predecessor != None:
                return node.predecessor

        return None

    def predecessor(self, val):

        node = self.longestPrefix(val)

        

        if type(node) == self.LeafNode:
            return node.left
        
        elif type(node) == self.InternalNode:

            print(node.val)
            if  node.predecessor != None:
                return node.predecessor

            if  node.successor != None:
                return node.successor
        
        return None



    def longestPrefix(self, val):
        #Start to search 


        #Doesn't Exist
 
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

        return self.layers[best][s]   


    def insert(self, val):

        #Value already exists
        if val in self.layers[0]:
            return


        node = self.LeafNode(val, self.predecessor(val), None)
        #print(node.left)
        self.layers[0][val] = node
        nodeptr = self.root

        bits = [1 if digit=='1' else 0 for digit in bin(val)[2:]]

        
        for i in range(self.u - 1):
            b = val >> i + 1
            
            if b not in self.layers[i+1].keys():
                
                tmpNode = self.InternalNode(b)

                
                if bits[self.u - 1 -i] == 0:
                    tmpNode.predecessor = node
                    tmpNode.left = node
                
                if bits[self.u - 1 -i] == 1:
                    tmpNode.successor = node
                    tmpNode.right = node

                self.layers[i+1][b] = tmpNode

                node = tmpNode
            
            #Node exists
            else:
                tmpNode = self.layers[i+1][b]

        #We Need To find successor
                if bits[self.u - 1 -i] == 0:
                    tmpNode.left = node
                    tmpNode.predecessor = node
                
                if bits[self.u - 1 -i] == 1:
                    tmpNode.right = node
                    tmpNode.successor = node

                node = tmpNode
                

    def print(self):

        for hashes in self.layers:
            print(hashes.keys())

    
        

x = xFast(4)

x.insert(12)
x.insert(13)
x.insert(15)
#x.print()

#print(x.layers[1][6].successor.val)