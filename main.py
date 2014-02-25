#! /usr/bin/env/python 

import re
from pprint import pprint
import numpy as np
import numpy.random as npr
import pylab

def readbook():
#    lines = [line.rstrip('\n').split(' ') for line in open('pg44777.txt')]
    f = open('pg44777.txt', 'r')     
    text = []
    for line in f:
        text.extend(line.split())
    return text 

def wordlen(text):
    d = {}
    for word in text:
        if len(word) in d:
            d[len(word)] += 1
        else:
            d[len(word)] = 1
    return d

def samplebook(text):
    sample = []
    i = 25
    j = 0
    print text[1]
    while(j <= i):
         #sample.extend(text[npr.randint(1,131544)])
         sample += [text[npr.randint(1,131544)]]
         j += 1
    pprint(sample)

def main():
    sweetBook = readbook()
    hissyGram = wordlen(sweetBook)
    pprint(hissyGram)
    samplebook(sweetBook)
    i = len(sweetBook)
    print i 
    print("fuck you book")

main()
