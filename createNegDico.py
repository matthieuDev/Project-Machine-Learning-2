#!/usr/bin/env python3
import pickle

#Use of codecs to be able to ierate on txt with string
import codecs

#Used to create csv file
import proj2_helpers as ph

#basic methods
import numpy as np

#method created
import util as u

def main() :
    dicos = u.downloadDico()
    
    falseFalsePosDico = dict()
    falseFalsePosDico2 = dict()
    truePosDico = dict()
    falsePosDico = dict()
    with codecs.open('train_pos_full.txt',encoding='utf-8') as f:
        for idx , line in enumerate(f):
            test = u.resWordMultipleDicosRet0(dicos, line)
            if ( test == [-1] ) :
                sentence = (''.join(line)).split()
                for word in sentence :
                   u.incrementDict (falseFalsePosDico , word , 1 )
            elif(test == [1]) :
                sentence = (''.join(line)).split()
                for word in sentence :
                   u.incrementDict (truePosDico , word , 1 )                

    for word in falseFalsePosDico :
        if  word not in truePosDico :
            falseFalsePosDico2[word] = falseFalsePosDico[word]

    
    for word in falseFalsePosDico2 :
        if ( falseFalsePosDico2[word] > len(falseFalsePosDico2)/1000) :
            falsePosDico[word] = 1
    print(falsePosDico)
        

    falseFalseNegDico = dict()
    falseFalseNegDico2 = dict()
    trueNegDico = dict()
    falseNegDico = dict()
    with codecs.open('train_neg_full.txt',encoding='utf-8') as f:
        for idx , line in enumerate(f):
            test = u.resWordMultipleDicosRet0(dicos, line)
            if ( test == [1] ) :
                sentence = (''.join(line)).split()
                for word in sentence :
                   u.incrementDict (falseFalseNegDico , word , 1 )
            elif(test == [-1]) :
                sentence = (''.join(line)).split()
                for word in sentence :
                   u.incrementDict (trueNegDico , word , 1 )

    for word in falseFalseNegDico :
        if  word not in trueNegDico :
            falseFalseNegDico2[word] = falseFalseNegDico[word]
            
    for word in falseFalseNegDico2 :
        if ( falseFalseNegDico2[word] > len(falseFalseNegDico2)/1000) :
            falseNegDico[word] = 1

    with codecs.open('dictionnaire/falseNegdico.txt','w','utf-8') as f :
        for word in falseNegDico :
            f.write (word + " " + str(falseNegDico[word]) + '\n')

    with codecs.open('dictionnaire/falsePosdico.txt','w','utf-8') as f :
        for word in falsePosDico :
            f.write (word + " " + str(falsePosDico[word]) + '\n')
            
    print(falseNegDico)
