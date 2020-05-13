from googletrans import Translator
import re
import pandas as pd

dictionaryFile = open('file.csv', 'r')
myDictFile = pd.read_csv('dict.csv', sep = ";")
words = dictionaryFile.read()
wordList = words.split(';')
englishWords = []
russianWords = []

# check mask for english words
english_check = re.compile(r'[a-z]')

for i in range(len(wordList)):
    if re.match(english_check, wordList[i]) != None:
        print(wordList[i])
        englishWords.append(wordList[i])
        # TODO разберись с этим говном
        russianWords.append(Translator.translate(text=wordList[i], dest='ru').text)
# TODO настроить нормальное добавление новых строк в словарь
for i in range(len(russianWords)):
    myDictFile = myDictFile.append([[englishWords[i], ' - ', russianWords[i]]])

myDictFile.to_csv("new_dict.csv")