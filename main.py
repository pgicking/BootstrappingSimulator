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
    minibook = text
     

def main():
    sweetBook = readbook()
    hissyGram = wordlen(sweetBook)
    pprint(hissyGram)
    print("fuck you book")

main()
