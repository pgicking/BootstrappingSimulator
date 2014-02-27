#! /usr/bin/env/python

# Copyright Clayton Ward and Peter Gicking
# Portland State University
# Stats 451
# Professor Blackmore


import re
from pprint import pprint
import numpy as np
import numpy.random as npr
import pylab
import random
import matplotlib as plt
from matplotlib import pyplot


#Reads the text from our book and stores each word in a list
def readBook():
    f = open('pg44777.txt', 'r')
    text = []
    for line in f:
        text.extend(line.split())
    return text

#Reads the list from readBook() and makes counts the length of each word
#and stores it in a dictionary
def wordLen(text):
    d = {}
    for word in text:
        if len(word) in d:
            d[len(word)] += 1
        else:
            d[len(word)] = 1
    return d

#This takes a list input and shuffles it and then takes the first j elements
#This is so we dont accidently "sample" from the same position twice
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

#Takes a subsample from the text to be iterated over
def subSample(text):
    idx = npr.randint(1,len(text),(len(text)))
    subSample = []
    for i in idx:
        subSample.append(text[i])
    print subSample
    return subSample

#creates a histogram of the dictionary passed in
def histoGram(d):
    pyplot.bar(d.keys(), d.values())
    pyplot.title( 'Bootstrapping')
    pyplot.xlabel( 'Word length' )
    pyplot.ylabel ( 'Number of Occurences' )
    pyplot.savefig( 'foo.png' )
    pyplot.show()
    
def test():
    X = range(0,100)
    Y = [ i*i for i in X ]
    
    pyplot.plot(X,Y, '-')
    pyplot.title( 'Plotting x*x' )
    pyplot.xlabel( 'X Axis' )
    pyplot.ylabel( 'Y Axis' )
    pyplot.savefig( 'Simple.png' )
    pyplot.show()

#Main function
def main():
    sweetBook = readBook()
    hissyGram = wordLen(sweetBook)
    sample = samplePop(sweetBook)
    bootstrap = subSample(sample)
    subhissygram = wordLen(bootstrap)
    histoGram(subhissygram)
    i = len(sweetBook)
    print i
    print("fuck")

#Executes main
main()
