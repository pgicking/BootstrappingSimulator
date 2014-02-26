#! /usr/bin/env/python 

import re
from pprint import pprint
import numpy as np
import numpy.random as npr
import pylab
import random

def readbook():
#    lines = [line.rstrip('\n').split(' ') for line in open('pg44777.txt')]
    f = open('pg44777.txt', 'r')     
    text = []
    for line in f:
        text.extend(line.split())
    return text 

def wordLen(text):
    d = {}
    for word in text:
        if len(word) in d:
            d[len(word)] += 1
        else:
            d[len(word)] = 1
    return d

def samplePop(text):
    sample = []
    random.shuffle(text)    
    i = 25
    j = 0
    dupe = []
    while(j <= i):
         sample += [text[j]]  
         j += 1
#    pprint(sample)
    return sample

def subSample(text):
    idx = npr.randint(1,len(text),(len(text)))
    subSample = []
    for i in idx:
        subSample.append(text[i])
    print subSample
    return subSample 

def main():
    sweetBook = readbook()
    hissyGram = wordLen(sweetBook)
    sample = samplePop(sweetBook)
    subSample(sample)
    i = len(sweetBook)
    print i 
    print("fuck you book")

main()
