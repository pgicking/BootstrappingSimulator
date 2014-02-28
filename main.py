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

def calcAvg(d):
    i = 0.0
    j = 0.0
    for x in d:
        i += d[x]*x
        j += x    
    avg = (i / j)
    return avg

#This takes a list input and shuffles it and then takes the first j elements
#This is so we dont accidently "sample" from the same position twice
def samplePop(text,sampleSize):
    sample = []
    random.shuffle(text)
    i = sampleSize
    j = 0
    dupe = []
    while(j <= i):
         sample += [text[j]]
         j += 1
#    pprint(sample)
    return sample

#Takes a subsample from the text to be iterated over
#Creates random numbers, then goes to the index to stores it
def subSample(text):
    idx = npr.randint(1,len(text),(len(text)))
    subSample = []
    for i in idx:
        subSample.append(text[i])
    print subSample
    return subSample

#creates a histogram of the dictionary passed in
def histogram(d,name):
    pyplot.bar(d.keys(), d.values())
    pyplot.title( 'Bootstrapping - ' + name )
    pyplot.xlabel( 'Word length' )
    pyplot.ylabel ( 'Number of Occurences' )
    pyplot.savefig( 'Bootstrap_' + name + '.pdf' )
#    pyplot.show()
    

#Main function
def main():
    name = 'Population'
    #read book and store it in population
    pop = readBook()
    #Sort by word length and store in popHist
    popHist = wordLen(pop)
    #Creates the population histogram
    #histogram(popHist,name)
    print '\nCreating Histogram of the Population\n'
   
    sampleNum = int(raw_input("\nHow big of a subsample would you like?:"))
    sample = samplePop(pop,sampleNum)    
    bootNum = int(raw_input("\nHow many times would you like to bootstrap?:"))
    i = 0
    j = bootNum
    bootStrap = {}
    d = {}
    while(i < j):
        i += 1        
        bootStrap = subSample(sample)
        words = wordLen(bootStrap)
        avg = calcAvg(words)
        round(avg)
        if avg in d:
            d[avg] += 1
        else:
            d[avg] = 1
    name = 'SubSample'
    histogram(d,name)        
    print d
    print("fuck")

#Executes main
main()
