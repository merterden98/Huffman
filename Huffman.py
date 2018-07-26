import queue
from bitarray import bitarray


class Huffman():

    
    class Node():

        def __init__(self, freq, letter):

            self.letter = letter
            self.freq = freq
            self.right = None
            self.left = None


        def __lt__(self, other):

            return self.freq < other.freq

    def __init__(self, filepath, queue):
        #TODO Open File and count letters.

        self.queue = queue
        self.filepath = filepath
        self.frequencies = {}
        self.codes = {}
        self.nodes = []


    def getfrequencies(self):

        with open(self.filepath, 'r') as f:
            
            for lines in f:
                for letter in lines:
                    if letter not in self.frequencies:
                        self.frequencies[letter] = 1
                    else:
                        self.frequencies[letter] += 1

            

    
    def makeInitialNodes(self):

        for letters in self.frequencies:
            node = self.Node(self.frequencies[letters], letters)
            self.nodes.append(node)
            self.queue.put(node)

    def makeTree(self):

        
        while(self.queue.qsize() > 1):
            
            n1 = self.queue.get()
            n2 = self.queue.get()

            parent = self.Node(n1.freq + n2.freq, None)
            parent.left = n1
            parent.right = n2
            self.queue.put(parent)

    
    def _make(self, node, code):

        if node == None:
            return
        
        #We are at a leaf character
        if node.letter != None:
            self.codes[node.letter] = code
            return
        
        self._make(node.left, code + '0')
        self._make(node.right, code + '1')




    
    def makeCodes(self):

        root = self.queue.get()     
        self._make(root, '')


    def compress(self):

        self.getfrequencies()
        self.makeInitialNodes()
        self.makeTree() 
        self.makeCodes()

        bray = bitarray()

        with open(self.filepath, 'r') as f:
            
            for lines in f:
                for letter in lines:
                     bray.extend(self.codes[letter])
        

        outfile = self.filepath + ".cmp"

        with open(outfile, 'wb') as f:
            bray.tofile(f)

        




q = queue.PriorityQueue()

H = Huffman("LargerFile", q)



H.compress()

