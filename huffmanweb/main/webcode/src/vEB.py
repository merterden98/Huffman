import math

class vEB():


    """u is defined as the size of the universe """
    def __init__(self, u):

        if u < 0:
            raise Exception("Size Has To Be Greater Than 0")
        
        self.max = None
        self.min = None

        self.qs = 0
        

        self.summary = None
        self.clusters = None
        self.u = 1
        self.u <<=int(math.log2(u))
        
        self.values = [0 for i in range(self.u)]

        if self.u > 2:
            self.clusters = [None for i in range(self.high(self.u) + 1)]
            self.summary = vEB(self.high(u))


    def get(self):

        #We Don't Need to Delete

        if self.min == None:
            return None

        tmp = self.values[self.min]

        self.qs -= 1

        if tmp.next != None:
            self.qs -= 1
            
            tmp = self.values[self.min]
            self.values[self.min] = tmp.next
            tmp.next = None
            return tmp

        else:
            newMin = self.successor(self.min)
            toReturn = self.values[self.min]
            self.values[self.min] = 0
            #print(f"Will Return {toReturn.letter} New Min {newMin}")
            self.delete(self.min)

            return toReturn

        

    def put(self, node):

        self.qs += 1

        if self.member(node.freq):
            #print(f"Already Here normally would insert {node.letter}")


            tmp = self.values[node.freq]

            node.next = tmp

            self.values[node.freq] = node
            
            


        else:
            self.insert(node.freq)
            self.values[node.freq] = node


    def qsize(self):
        return self.qs


    def high(self, lookup):

        return math.floor(lookup / math.sqrt(self.u))

    def low(self, lookup):

        return lookup % math.ceil(math.sqrt(self.u))

    def index(self, cluster, offset):
        pass

    def member(self, lookup):

        if lookup == self.min or lookup == self.max:
            return True
        
        #We reached smallest cluster size
        elif self.u <= 2:
            return False
        
        else:
            #Cluster Was Never Initialized
            if self.clusters[self.high(lookup)] == None:
                return False

            return self.clusters[self.high(lookup)].member(self.low(lookup))

    def leaf_insert(self, val):
        self.max = val
        self.min = val

    def index(self, high, offset):

        return high * math.floor(math.sqrt(self.u)) + offset
    
    def successor(self, val):

        #Smallest Substructure We Can Get
        if self.u <= 2:
            if val == 0 and self.max == 1:
                return 1
            else:
                return None
        
        #We Reached the cluster and successor is that clusters min
        elif self.min != None and val < self.min:
            return self.min

        else:
            if self.clusters[self.high(val)] != None:
                mLow = self.clusters[self.high(val)].max
                
                if mLow != None:
                    #We are in correct cluster and need to find
                    #offset in cluster
                    if mLow > self.low(val):
                        offset = self.clusters[self.high(val)].successor(self.low(val))
                        return self.index(self.high(val), offset)

            #We Have to go to a different cluster (Go Up)
            else:

                succcluster = self.summary.successor(self.high(val))

                #Successor Doesn't Exist
                if succcluster == None:
                    return None
                
                else:
                    #minimum of the next cluster
                    offset = self.clusters[succcluster].min
                    return self.index(succcluster, offset)


    def insert(self, val):

        

        if self.min == None:
            self.leaf_insert(val)
            return

        if val < self.min:
            tmp = self.min
            self.min = val
            val = tmp

        #This is the Index of the element within cluser
        i = self.low(val)

        #This is the Index of the cluster
        j = self.high(val)
        
        #We Still Have to recurse into SubArrays
        if self.u > 2:

            if self.clusters[j] == None:
                self.clusters[j] = vEB(self.high(self.u))
            
            #Cluster Hasn't Been Accessed Before
            if self.clusters[j].min == None:
                self.clusters[j].leaf_insert(i)
                self.summary.insert(j)
            else:
                self.clusters[j].insert(i)    


        if val > self.max:
            self.max = val

    def deleteOrg(self, val):
        
        self.qs -= 1
        #Only element in Tree
        if self.min == self.max and self.min == val:
            self.min = None
            self.max = None
            return


                
        #We found min value and need next minimum to replace it
        if self.min == val:

            if self.summary != None and self.summary.min != None:
                cluster_index = self.summary.min
                element_index = self.clusters[cluster_index].min

                val = self.index(cluster_index, element_index)
                self.min = val
        
        #Finding What Cluster Element Belongs To
        cluster_index = self.high(val)
        element_index = self.low(val)

        if self.clusters == None:
            return

        if self.clusters[cluster_index] == None:
            return
        
        self.clusters[cluster_index].delete(element_index)

        #if cluster is empty remove it from summary
        if self.clusters[cluster_index].min == None:
            self.summary.delete(cluster_index)

        
        if val == self.max:
            
            #if we delete max, min becomes new max
            if self.summary.max == None:
                self.max = self.min
                return
        
        #Otherwise Max is next Max
        cluster_index = self.summary.max
        element_index = self.clusters[cluster_index].max
        self.max = self.index(cluster_index, element_index)


    def delete(self, val):

        

        if self.min is None or val < self.min:
            return
        
        

        if val == self.min:
            if self.summary is None or self.summary.min is None:
                self.min = self.max = None
                return
            cluster_index = self.summary.min
            element_index = self.clusters[cluster_index].min

        
            val = self.min = self.index(cluster_index, element_index)

        cluster_index = self.high(val)
        element_index = self.low(val)
        cluster = self.clusters[cluster_index]
        
        if cluster is None:
            return

        cluster.delete(element_index)

        if cluster.min is None:
            self.summary.delete(cluster_index)

        if val == self.max:
            if self.summary.max is None:
                self.max = self.min
            else:
                cluster_index = self.summary.max
                element_index = self.clusters[cluster_index].max
                self.max = self.index(cluster_index, element_index)

        

##Reference http://www-di.inf.puc-rio.br/~laber/vanEmdeBoas.pdf