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
import re

dictPath = "dict.csv"  # route to words

# TODO отдебажились нормально. надо пробегаться по папке с целевым файлом, искать ключевое слово
# далее сравнивать дату изменения с изменением главного словаря, и обновлять словарь
# используй stat = os.stat(path) и stat.st_mtime
# i need to move data from one csv to another
class FavouriteDict():
    def __init__(self, favDictPath, mainDictPath):
        self.favDictPath = favDictPath
        self.mainDictPath = mainDictPath
    def loadNewWords(self):
        favPd = pd.read_csv(self.favDictPath, sep=';', header=None)
        mainPd = pd.read_csv(self.mainDictPath, sep=';')
        newDf = pd.DataFrame(list(zip(list(favPd[2]), [''] * favPd.shape[0], list(favPd[3]))),\
                             columns=['word', 'transcript', 'translate'])
        mainPd = mainPd.append(newDf, ignore_index=True)
        mainPd.to_csv(self.mainDictPath, index=False)

class Game():
    def __init__(self, dictPath):
        self.dictPath = dictPath
        self.badAnswers = ['Lol, no', 'Try better', 'U made me cry, loser', 'Nope']
        self.yesAnswers = ['Good!', 'Hell, yeah!', '^=^ you are the best!', 'Yep']
        self.usedIndexes = []  # array with used indexes of words from dict
        self.score = 0

    def updateDict(self):
        dictDf = pd.read_csv(self.dictPath, sep=";")
        dictDf = dictDf.fillna("")
        self.words = dictDf['word'].tolist()
        self.transcript = dictDf['transcript'].tolist()
        self.translate = dictDf['translate'].tolist()

    def play(self):
        flag = 0
        while flag == 0:
            myIndex = randint(0, len(self.words))
            firstWrong = randint(0, len(self.words))
            secondWrong = randint(0, len(self.words))
            thirdWrong = randint(0, len(self.words))
            if myIndex in self.usedIndexes or myIndex in [firstWrong, secondWrong, thirdWrong]:
                pass
            else:
                self.usedIndexes.append(myIndex)
                flag = 1
        print("I have this word: \n", self.words[myIndex], " ", self.transcript[myIndex])
        print("Choose the right translation: (type digit from 1 to 4)")
        time.sleep(2)
        order = [str(self.translate[firstWrong]), \
             str(self.translate[secondWrong]), \
             str(self.translate[thirdWrong]), \
             str(self.translate[myIndex])]
        shuffle(order)  # random mixing of translations
        rightIndex = order.index(str(self.translate[myIndex])) + 1  # detect number of corrrect answer

        print("1 ", order[0])
        print("2 ", order[1])
        print("3 ", order[2])
        print("4 ", order[3])

        userAnswer = int(input())
        time.sleep(1)
        if userAnswer == rightIndex:
            print(self.yesAnswers[randint(0, len(self.yesAnswers) - 1)], "\n")
            self.score += 1
        else:
            print(self.badAnswers[randint(0, len(self.badAnswers) - 1)], "\n The right answer is: ", (rightIndex))

def main():
    print("How many rounds do you want to play?")
    flag = 0
    while flag == 0:
        print("Type the digit from 1 to 9. X to exit")
        userInput = input()
        if re.match('[1-9]', userInput) != None:
            flag = 1
        elif userInput.lower() == 'x':
            return "Bye!"
    myGame = Game(dictPath)
    myGame.updateDict()  # update dictionary with words
    for i in range(int(userInput)):
        myGame.play()
    print ("Your score is: " + str(myGame.score))
    return 0

main()

