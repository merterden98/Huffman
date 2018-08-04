import queue
from yFast import yFast
from bitarray import bitarray
from vEB import vEB


class Huffman():

    
    class Node():

        def __init__(self, freq, letter):

            self.letter = letter
            self.freq = freq
            self.right = None
            self.left = None
            self.next = None

        def __lt__(self, other):

            return self.freq < other.freq

    def __init__(self, queue, filepath=None):
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

            
            #print(self.frequencies)
            
                


            

    
    def makeInitialNodes(self):

        for letters in self.frequencies:
            node = self.Node(self.frequencies[letters], letters)
            self.nodes.append(node)
            #print("Placing Node")
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

        self.root = self.queue.get()     
        self._make(self.root, '')


    def compress(self):

        self.getfrequencies()
        self.makeInitialNodes()
        self.makeTree() 
        self.makeCodes()

        bray = bitarray()

        outfile = self.filepath + ".cmp"
        key = '.' + self.filepath + ".key"


        with open(self.filepath, 'r') as f:
            
            for line in f:
                for char in line:
                    bray.extend(self.codes[char])

        with open(outfile, 'wb') as f:
            
            t = self.makeBitTree() 
            bray.tofile(f)


        with open(key, 'w') as b:
            b.write(t)
        
    def makeBitTree(self):

        txt = []

        self.bitHelp(self.root, txt)

        l = ""

        for word in txt:
            l = l + word
        
        return l
        
        
    
    def bitHelp(self, node, txt):

        for keys in self.codes.keys():
            txt.append(self.codes[keys])
            txt.append(keys)

        


    def bitDecodeTree(self, txt):

        if len(txt) == 0:
            return

        if txt.pop(0) == '1':
            char = ""
            for i in range(8):
                if len(txt) > 0:
                    char = char + txt.pop(0)
                
            print(char)
            
            return self.Node(0, 'a')
            
        else:
            txt.pop(0)
            left = self.bitDecodeTree(txt)
            right = self.bitDecodeTree(txt)
            node = self.Node(0, None)
            node.right = right
            node.left = left
            return node
        
    
    def decompress(self, cmpfile):

        decomp = {}
        keyfile = "." + cmpfile[:len(cmpfile)-3] + 'key'

        with open(keyfile, 'r') as f:
            code = []
            for line in f:
                for letter in line:
                    
                    if letter == '0' or letter == '1':
                        code.append(letter)
                    
                    else:
                        c = ''.join(code)
                        decomp[c] = letter
                        code = []
        
        #print("Decompress Table,",decomp)
        root = self.makeDTree(decomp)
        x = bitarray()     
        tmp = root  

        d = cmpfile[:len(cmpfile)-3] + "txt"
        with open(cmpfile, 'rb') as f:

            with open(d, 'w') as w:

                x.fromfile(f)

                for bits in x:
                
                    if bits == True:
                        tmp = tmp.right

                        if tmp == None:
                            tmp = root
                            pass

                        if tmp.letter != None:
                            w.write(tmp.letter)
                            tmp = root
                
                    if bits == False:
                        tmp = tmp.left
                    
                        if tmp == None:
                            tmp = root
                            pass

                        if tmp.letter != None:
                            w.write(tmp.letter)
                            tmp = root

            
                       


    def makeDTree(self, decomp):

        root = self.Node(None, None)
        for keys in decomp:
            node = root
            for b in keys:
                if b == '0':
                    if node.left == None:
                        tmp = self.Node(None, None)
                        node.left = tmp
                    node = node.left
                if b == '1':
                    if node.right == None:
                        tmp = self.Node(None, None)
                        node.right = tmp
                    node = node.right
            
            node.letter = decomp[keys]
        
        return root
                

                

