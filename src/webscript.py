from vEB import vEB
from yFast import yFast
from HuffmanWeb import Huffman
import queue
import time

def timeCompress(text):

    info = {}

    q = queue.PriorityQueue()

    binaryHuffman = Huffman(text, q)
    start = time.time()
    string, codes = binaryHuffman.compressWeb()
    end = time.time()
    info['string'] = string
    info['codes'] = codes
    info['bintime'] = end-start

    info['avgLen'] = averageCodeLength(codes)


    q = vEB(256)
    #print("Making van Emde Boas")
    vEBHuffman = Huffman(text, q)
    vEBHuffman.getfrequencies()
    start = time.time()
    vEBHuffman.makeInitialNodes()
    end = time.time()
    vEBHuffman.makeTree()
    info['vEbtime'] = end-start
    #print("Done with vEB took:", (end-start))

    q = yFast(1000)
    #print("Making yFast")
    yFastHuffman = Huffman(text, q)
    yFastHuffman.getfrequencies()
    start = time.time()
    yFastHuffman.makeInitialNodes()
    end = time.time()
    yFastHuffman.makeTree()
    info['yFasttime'] = end-start
    #print("Done with yFast took:", (end-start))

    return info


def averageCodeLength(codes):

    codeLen = 0

    for values in codes.values():

        codeLen += len(values)

    return codeLen/len(codes)

    


