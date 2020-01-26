# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:52:43 2019

@author: hcani
"""

path = "dict.csv" # path to your excel dict
import pandas as pd
import time
from random import randint
from random import shuffle
from googletrans import Translator

class Game():
    def __init__(self, dictPath, countOfRounds):
        self.dictPath = dictPath
        self.countOfRounds = countOfRounds
        self.badAnswers = ['Lol, no', 'Try better', 'U made me cry, loser', 'Nope']
        self.yesAnswers = ['Good!', 'Hell, yeah!', '^=^ you are the best!', 'Yep']

    def updateDict(self):
        dictDf = pd.read_csv(dictPath, sep=";")
        dictDf = dictDf.fillna("")
        self.words = dictDf['word'].tolist()
        self.transcript = dictDf['transcript'].tolist()
        self.translate = dictDf['translate'].tolist()

    def play(self):




def updateDict(rout):
    dictDf = pd.read_csv(rout, sep = ";")
    dictDf = dictDf.fillna("")
    words = dictDf['word'].tolist()
    transcript = dictDf['transcript'].tolist()
    translate = dictDf['translate'].tolist()
    return([words, transcript, translate])

def training(words, transcript, translate):
    print("How many rounds do you want? (type integer digit)")
    count = int(input()) # count of rounds
    #rate = 0
    pastmyIndexes = [] # что это такое блят
    badAnswers = ['Lol, no', 'Try better', 'U made me cry, loser', 'Nope']
    yesAnswers = ['Good!', 'Hell, yeah!', '^=^ you are the best!', 'Yep']
    score = 0
    for i in range(count):
        print("Okay dude, be patient...\n")
        time.sleep(1)                                                                                                                                                                                                                                                              
        flag = 0
        while flag == 0:
            myIndex = randint(0, len(words))
            firstWrong = randint(0, len(words))
            secondWrong = randint(0, len(words)) 
            thirdWrong = randint(0, len(words))
            if myIndex in pastmyIndexes or myIndex in [firstWrong, secondWrong, thirdWrong]:
                pass
            else:
                pastmyIndexes.append(myIndex)
                flag = 1
                
        print("I have this word: \n", words[myIndex], " ", transcript[myIndex], "\n")
        print("Choose the right translation: (type integer digit from 1 to 4)")
        time.sleep(2)
        
        order = [str(translate[firstWrong]), \
                 str(translate[secondWrong]), \
                 str(translate[thirdWrong]), \
                 str(translate[myIndex])]
        shuffle(order) # random mixing of translations
        rightIndex = order.index(str(translate[myIndex])) + 1 # detect number of corrrect answer
        
        print("1 ", order[0])
        print("2 ", order[1])        
        print("3 ", order[2])
        print("4 ", order[3])
        
        userAnswer = int(input())
        time.sleep(1)  
        if userAnswer == rightIndex:
            print(yesAnswers[randint(0, len(yesAnswers)-1)], "\n")
            score += 1
        else:
            print(badAnswers[randint(0, len(badAnswers)-1)], "\n The right answer is: ", (rightIndex))
    print("Your score is: ", score, "/", count)
            
        

check = updateDict(path)
training(check[0], check[1], check[2])
