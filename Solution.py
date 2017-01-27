#!/usr/bin/env python3
import pickle

#Use of codecs to be able to ierate on txt with string
import codecs

#Used to create csv file
import proj2_helpers as ph

#basic methods
import numpy as np

import util as u

i = 0 
def main():
    #number of tweet in the train
    tweetNumber = 100000
    dicos = u.downloadDico()
    doubleDicos = u.downloadDoubleDico()
#    multiDicos = u.downloadMultiDico()
#    [falsePosDico,falseNegDico] = u.downloadNegDico()
    
    res= []
    
    with codecs.open('test_data.txt',encoding='utf-8') as f:
        for  line in f:
#            res = res + u.resMultiWord(multiDicos , line)
            res = res + u.resWordWithDouble ( dicos , line, doubleDicos)
#            res = res + u.resWordWithNeg ( dicos , line, falsePosDico,falseNegDico) 
 #           res = res + u.resWordMultipleDicosRet1(dicos, line) 
 #           res = res + u.resWordDoubleDico ( dico , bigDico , line) 

    ph.create_csv_submission(range(1,len(res)+1), res, "result.csv") 

if __name__ == '__main__':
    main()

