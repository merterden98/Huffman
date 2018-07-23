import math

class vEB():


    """u is defined as the size of the universe """
    def __init__(self, u):

        if u < 0:
            raise Exception("Size Has To Be Greater Than 0")
        
        self.max = None
        self.min = None

        self.u = 1
        self.u <<=int(math.log2(u))
        
        if self.u > 2:
            self.clusters = [None for i in range(self.high(self.u) + 1)]
            self.summary = vEB(self.high(u))

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
            if self.clusters[self.high(lookup)] == 0:
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
                print(mLow)
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
        print(j)
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


##Reference http://www-di.inf.puc-rio.br/~laber/vanEmdeBoas.pdf