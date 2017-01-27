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

i = 0 
def main():
    falseDico = [dict(),dict(),dict(),dict()]
    #number of tweet in the train
    tweetNumber = 100000
    
    with codecs.open('train_neg_full.txt',encoding='utf-8') as f:
        for line in f:
            sentence = (''.join(line)).split()
            for i in range (len(sentence)-1):
                toAdd = ''
                for j in range (4) :
                    if ( i < len(sentence )- j):
                        toAdd=toAdd+' '+sentence[i+j]
                        u.incrementDict (falseDico[j] , toAdd, -1 )

    with codecs.open('train_pos_full.txt',encoding='utf-8') as f:
        for line in f:
            sentence = (''.join(line)).split()
            for i in range (len(sentence)-1):
                toAdd = ''
                for j in range (4) :
                    if ( i < len(sentence )- j):
                        toAdd=toAdd+' '+sentence[i+j]
                        u.incrementDict (falseDico[j] , toAdd, 1 )
    
    dicos = [[dict(),dict(),dict(),dict()],
             [dict(),dict(),dict(),dict()],
             [dict(),dict(),dict(),dict()],
             [dict(),dict(),dict(),dict()]]


    
    for i in range(4) :
        for j in range(4) :
            for word in falseDico[i] :
                if (falseDico[i][word] > 10**(3-j) or falseDico[i][word] < -10**(3-j)) :
                   dicos[i][j][word]=falseDico[i][word]
                


    del falseDico

    res = []

    for i in range (4) :
        for j in range(4) :
            with codecs.open('dictionnaire/dicothresh'+str(i)+'multi'+str(j)+'.txt','w','utf-8') as f :
                for word in dicos[j][i] :
                    f.write (word + " " + str(dicos[j][i][word]) + '\n')
    
if __name__ == '__main__':
    main()
