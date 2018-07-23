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
            self.clusters = [0 for i in range(self.high(self.u) + 1)]
            self.summary = vEB(self.high(u))

    def high(self, lookup):

        return math.floor(lookup / math.sqrt(self.u))

    def low(self, lookup):

        return lookup % math.ceil(math.sqrt(self.u))


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
        print("Here")

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

            if self.clusters[j] == 0:
                self.clusters[j] = vEB(self.high(self.u))
            
            #Cluster Hasn't Been Accessed Before
            if self.clusters[j].min == None:
                self.clusters[j].leaf_insert(i)
                print("Inserting Into Summary")
                self.summary.insert(j)
            else:
                print("Going into Subcluster of Size {}".format(self.high(self.u)))
                print("To index {}".format(i))
                self.clusters[j].insert(i)    


        if val > self.max:
            self.max = val


##Reference http://www-di.inf.puc-rio.br/~laber/vanEmdeBoas.pdf