import queue
import time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
# Create your views here.

from .forms import TestForm
# from .webcode.src import vEB
# from .webcode.src import xFast
# from .webcode.src import yFast
# from .webcode.src import Huffman
from .vEB import vEB
from .xFast import xFast
from .yFast import yFast
from .HuffmanWeb import Huffman

#from .webscript import *


def index(request):
    return HttpResponse("Hello Again")



class home(TemplateView):
    
    template_name = "bootstrap/example.html"


    def get(self, request):

        form = TestForm()
        print('at get request')

        return render(request, self.template_name, {'form' : form} )

    def post(self, request):
        
        form = TestForm(request.POST)

        text = form.data['sample_data']

        print("hello")

        redirect = self.template_name

        return HttpResponseRedirect('demo/')
        #return render(request, redirect, {'form' : form})





class demo(TemplateView):


    template_name = "bootstrap/demo.html"


    def get(self, request):

        form = TestForm()

        return render(request, self.template_name, {'form' : form})


    def post(self, request):

        form = TestForm(request.POST)



        if form.is_valid():

            text = form.cleaned_data['data']

            entropy = self.findEntropy(text)

            getData = self.timeCompress(text)

            print(getData)

           
            p = {'form': form, 'text' : entropy, 'sampledata': 'data'}

            args = {**p, **getData}

        return render(request, self.template_name, args)


    def findEntropy(self, text):

        import math

        freq = {}

        for letter in text:

            if letter not in freq:
                freq[letter] = 1

            else:
                freq[letter] += 1

        
        total = 0

        for val in freq.values():

            total += val

        
        ent = 0.0

        for val in freq.values():

            ent -= (val/total) * math.log2((val/total))
        
        return ent

    def timeCompress(self, text):

        info = {}

        q = queue.PriorityQueue()

        binaryHuffman = Huffman(text, q)
        start = time.time()
        string, codes = binaryHuffman.compressWeb()
        end = time.time()
        info['string'] = string
        info['codes'] = codes
        info['bintime'] = (end-start)*100

        info['avgLen'] = self.averageCodeLength(codes)


        q = vEB(256)
        #print("Making van Emde Boas")
        vEBHuffman = Huffman(text, q)
        vEBHuffman.getfrequencies()
        start = time.time()
        vEBHuffman.makeInitialNodes()
        end = time.time()
        vEBHuffman.makeTree()
        info['vEbtime'] = (end-start)*100
        #print("Done with vEB took:", (end-start))

        q = yFast(1000)
        #print("Making yFast")
        yFastHuffman = Huffman(text, q)
        yFastHuffman.getfrequencies()
        start = time.time()
        yFastHuffman.makeInitialNodes()
        end = time.time()
        yFastHuffman.makeTree()
        info['yFasttime'] = (end-start)*100
        #print("Done with yFast took:", (end-start))

        return info


    def averageCodeLength(self, codes):

        codeLen = 0

        for values in codes.values():

            codeLen += len(values)

        return codeLen/len(codes)

    



        
        
