from .xFast import xFast
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

        self.qs = 0

        
    def qsize(self):

        return self.qs

    def get(self):
        
        
        temp = self.min

        #print("Will Return ", temp.letter)

        p = self.delete(temp.freq)

        

        if p == True:

            self.min = temp.next

        else:
            #print("Need To find Successor")
            #print("temp val:", temp.freq)
            mn, index = self.successor(temp.freq)
            #print(self.subtrees)
            #print(mn, index)

            if mn == None or index == None:
                self.min = None
                return temp

            self.min = self.subtrees[index][mn]
        
        return temp


    def successor(self, search):

        #print(f"Finding Successor {search}")
        logSearch = search
        s = self.summary.successor(logSearch)

        if s is not None:

            subtreeIndex =  math.floor(s.val / math.log2(self.size))

            
    

            succ = s.val

            for items in self.subtrees[subtreeIndex].keys():

                if items > search and items < succ:
                    succ = items


            #print("Successor: ", succ)
            return succ, subtreeIndex
        
        else:
            return None, None 
        

    def put(self, node):

        self.insert(node, node.freq)



    def insert(self, val, key):

        #print(f"Value {val}, Key {key}")

        if self.min == None:
            self.min = val

        else:
            if val < self.min:
                self.min = val

        logSearch = key - 1


        s = self.summary.successor(logSearch)

        
        
        if s is None:
            self.summary.insert(key)
            #print(f"Inserted {logSearch} into Summary")

            if key > 1:
                s = math.floor(key / math.log2(self.size))

            else:
                s = 0

            #print("S", s)
        

        else:
            if logSearch <= 1:
                s = 0
            else:
                lg = math.floor(s.val / math.log2(self.size))
                s = lg
        

       
        if key in self.subtrees[s]:
           # print(f"Val {val.letter} in {s}")
            tmp = self.subtrees[s][key]

            while tmp.next != None:
                #print(f"Adding to {tmp.letter}")
                tmp = tmp.next
            
            tmp.next = val
            self.qs += 1
            return

        

        self.subtrees[s][key] = val

        if len(self.subtrees[s]) > 2*self.log:
            l = []
            

            for keys, values in self.subtrees[s]:
                if keys < key:
                    l.append((keys, values))
            
            l.append((key, val))

            print(l)

            for pops in l:
                self.subtrees[s].pop(pops[0])



            m = max(l)

            

            self.summary.insert(m[0])

            mlog =  math.floor(m / math.log2(self.size))
            
            for items in l:
                self.subtrees[mlog][items] = items

        
        self.qs += 1


    def delete(self, val):

        logSearch = val - 1
        s = self.summary.successor(logSearch)

        

        if s is not None:

            s = math.floor(val / math.log2(self.size))

           # print(s)
            
            if self.subtrees[s][val].next == None:
                self.subtrees[s].pop(val)
                rt = False

            else:

                self.subtrees[s][val] = self.subtrees[s][val].next
                rt = True

            if len(self.subtrees[s]) == 0:
                self.summary.delete(val)
        


            self.qs -= 1

            return rt
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


