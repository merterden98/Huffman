from xFast import xFast
import math



class yFast():

    class yFastNode():

        def __init__(self, LeftChild, RightChild, val):
            
            self.size = 1

            self.val = val
            self.Left = LeftChild
            self.Right = RightChild

        def __str__(self):

            return str(self.val)



    def __init__(self, u):

        self.size = u

        self.min = None

        self.summary = xFast(self.size)

        self.log = int(math.log2(u))

        self.subtrees = [{} for i in range(self.log + 1)]

        
    def extract_min(self):
        
        print("Old Min,", self.min)
        temp = self.min

        self.delete(temp)

        self.min = self.successor(temp)
        
        return temp


    def successor(self, search):

        logSearch = search - 1
        s = self.summary.successor(logSearch)

        if s is not None:

            subtreeIndex = int(math.log2(s.val))
            
            succ = s.val

            for items in self.subtrees[subtreeIndex].keys():

                if items > search and items < succ:
                    succ = items

            return succ
        
        else:
            return None  
        

    
    def insert(self, val):

        if self.min == None:
            self.min = val

        else:
            if val < self.min:
                self.min = val

        logSearch = val
        s = self.summary.successor(logSearch)

        
        
        if s is None:
            self.summary.insert(logSearch)
            #print(f"Inserted {logSearch} into Summary")
            
            s = int(math.log2(logSearch))
        
        else:
            lg = int(math.log2(s.val))
            s = lg
        

        self.subtrees[s][val] = val

        if len(self.subtrees[s]) > 2*self.log:
            l = []

            for items in self.subtrees[s].values():
                if items < val:
                    l.append(items)
            
            l.append(val)

            for pops in l:
                self.subtrees[s].pop(pops)



            m = max(l)

            

            self.summary.insert(m)

            mlog = int(math.log2(m))
            
            for items in l:
                self.subtrees[mlog][items] = items

        
        print(self.subtrees)


    def delete(self, val):

        logSearch = val - 1
        s = self.summary.successor(logSearch)

        

        if s is not None:

            s = int(math.log2(s.val))
            
            self.subtrees[s].pop(val)

            if len(self.subtrees[s]) == 0:
                self.summary.delete(val)
        
        else:
            pass
            




            


        
        

    
    def BSTinsert(self, root, val):

        if root == None:

            return self.yFastNode(None, None, val)

        
        else:

            if val > root.val:

                root.Right = self.BSTinsert(root.Right, val)
                root.size += 1
                return root


            else:

                root.Left = self.BSTinsert(root.Left, val)
                root.size += 1
                return root

    
    def BSTsplit(self, root):

        if root.Right != None:
            
            root.size -= root.Right.size
            root.Right = None
            return root.Right
        
        else:
            tmp = root
            tmpL = root.Left
            tmp.size = 1
            tmp.Left = None
            

            return tmpL, tmp


y = yFast(15)

y.insert(9)
y.insert(6)
y.insert(7)
y.insert(5)
y.insert(4)
y.insert(8)
y.insert(3)
y.insert(1)
y.insert(2)


        
