#!/usr/bin/env python3
import pickle

#Use of codecs to be able to ierate on txt with string
import codecs

#Used to create csv file
import proj2_helpers as ph

#basic methods
import numpy as np


# add word to the dictionnary
def incrementDict (dico , word , add ) :
    try :
        dico[word] = dico[word] + add
    except KeyError :
        dico[word] = add

#base algo
def resWordBasic ( dico , line) :
    return [valueWordNumber(dico,line)]

def resWordDoubleDico ( dico , bigDico , line) :
    res = valueWordNumber(dico,line)
    if (res == [0]) :
        return [valueWordNumber(bigDico,line)]
    else :
        return [res]
    
#for result
def resWordMultipleDicosRet1 ( dicos , line) :
    for i in range(len(dicos)) :
        res = valueWordNumber(dicos[i],line)
        if (res != [0]) :
            return [res]
    #If no result found return a random value
    return [1]

#for test
def resWordMultipleDicosRet0 ( dicos , line) :
    for i in range(len(dicos)) :
        res = valueWordNumber(dicos[i],line)
        if (res != [0]) :
            return [res]
    #If no result found return a random value
    return [0]

def resWordWithNeg ( dicos , line, falsePosDico,falseNegDico) :
    res = resWordMultipleDicosRet0 ( dicos , line)
    if ( res == [-1] ) :
        sentence = (''.join(line)).split()
        for word in falseNegDico :           
            if word in sentence :
                return [1]
        return res
    elif(res == [1] ) :
        sentence = (''.join(line)).split()
        for word in falsePosDico :           
            if word in sentence :
                return [-1]
        return res
    else :
        return [1]

def resWordWithDouble  ( dicos , line, doubleDicos) :
    for i in range(len(dicos)) :
        sentence = (''.join(line)).split()
        res = 0
        for word in range (len(sentence)-1) :
            doubleword = (sentence[word ] + " " + sentence[word+1] )
            res = res + np.sign(happyValue(doubleDicos[i],doubleword) )*2
        for word in sentence :
            res = res + np.sign(happyValue(dicos[i],word))
        if (res != [0]) :
            return [np.sign(res)]
    #If no result found return a random value
    return [1]

def resMultiWord (multiDicos, line ) :
    for i in range(len(multiDicos)) :
        sentence = (''.join(line)).split()
        res = 0
        for j in range (len(sentence)):
                toCompare = ''
                for k in range (4) :
                    if ( j < len(sentence )- k):
                        toCompare=toCompare+' '+sentence[j+k]
                        res = res + np.sign(happyValue(multiDicos[i][k],toCompare) )*k
        
        if (res != [0]) :
            return [np.sign(res)]
    #If no result found return a random value
    return [1]

#value to put into the result
def valueWordValue ( dico , line) :
    sentence = (''.join(line)).split()
    count = 0
    for word in sentence :
        count = count + happyValue(dico,word)
    return np.sign(count)

#value to put into the result
def valueWordNumber ( dico , line) :
    sentence = (''.join(line)).split()
    count = 0
    for word in sentence :
        count = count + np.sign(happyValue(dico,word))
    return np.sign(count)


#value to put into the result
def valueWordMixValueNumber ( dico , line) :
    sentence = (''.join(line)).split()
    countValuePos = 0
    countValueNeg = 0

    countNumberNeg = 0
    countNumberPos = 0
    for word in sentence :
        valWord = happyValue(dico,word)
        if ( valWord < 0 ) :
            countNumberNeg = countNumberNeg + 1
            countValueNeg = countValueNeg - valWord
        elif ( valWord > 0 ) :
            countValuePos = countValuePos + valWord
            countNumberPos = countNumberPos + 1

    countValue = countValuePos - countValueNeg
    countNumber = countNumberPos - countNumberNeg

    if ( countNumberNeg == 0 or countValueNeg==0 ) :
        if ( countValuePos == 0 and countNumberPos == 0 ) :
#if all is 0 return arbitrary value
            return 1
        else :
            return 1
    elif ( countNumberPos == 0 or countValuePos == 0 ) :
        return -1
    elif ( np.sign(countValue) == np.sign(countNumber)) :
        return np.sign(countValue)
    else :
        if ( np.max ([countNumberPos ,countNumberNeg])/ np.min ([countNumberPos ,countNumberNeg])
             >=  np.max ([countValuePos ,countValueNeg]) /  np.min ([countValuePos ,countValueNeg])) :
            return np.sign( countNumber)
        else :
            return np.sign(countValue)
    


#value given by the dictionnary, if there is none return 0
def happyValue ( dico , word ) :
    try :
        return dico[word] 
    except KeyError :
        return 0

#
def downloadDico() :
    res = []
    
    for i in range(4) :
        with codecs.open('dictionnaire/dico'+str(i)+'.txt',encoding='utf-8') as f :
            dico = dict()
            for line in f:
                sentence = (''.join(line)).split()
                dico[sentence[0]] = int(sentence[1])
            res = res + [dico]
    return res

def downloadDoubleDico() :
    res = []
    
    for i in range(4) :
        with codecs.open('dictionnaire/doubledico'+str(i)+'.txt',encoding='utf-8') as f :
            dico = dict()
            for line in f:
                sentence = (''.join(line)).split()
                dico[sentence[0]+" "+sentence[1]] = int(sentence[2])
            res = res + [dico]
    return res

def downloadNegDico() :
    res = []
    with codecs.open('dictionnaire/falseNegdico.txt',encoding='utf-8') as f :
        dico = dict()
        for line in f:
            sentence = (''.join(line)).split()
            dico[sentence[0]] = int(sentence[1])
        res = res + [dico]

    with codecs.open('dictionnaire/falsePosdico.txt',encoding='utf-8') as f :
        dico = dict()
        for line in f:
            sentence = (''.join(line)).split()
            dico[sentence[0]] = int(sentence[1])
        res = res + [dico]
        
    return res

def downloadMultiDico() :
    res = [[],[],[],[]]
    
    for i in range(4) :
        subres = []
        for j in range(4):
    
            with codecs.open('dictionnaire/dicothresh'+str(i)+'multi'+str(j)+'.txt',encoding='utf-8') as f :
                dico = dict()
                for line in f:
                    sentence = (''.join(line)).split()
                    toAdd = ''
                    for k in range (len(sentence)-1) :
                        toAdd = toAdd +' '+ sentence[k]
                    dico[toAdd] = int(sentence[len(sentence)-1])
                subres = subres + [dico]
        res[i] = subres
    return res
