from googletrans import Translator
import re
import pandas as pd

dictionaryFile = open('file.csv', 'r')
myDictFile = pd.read_excel('dict.xlsx')
words = dictionaryFile.read()
wordList = words.split(';')
englishWords = []
russianWords = []

# check for english words
english_check = re.compile(r'[a-z]')

for i in range(len(wordList)):
    if re.match(english_check, wordList[i]) != None:
        englishWords.append(wordList[i])
        russianWords.append(translator.translate(wordList[i], dest = 'ru').text)
# TODO настроить нормальное добавление новых строк в словарь
for i in range(len(russianWords)):
    myDictFile = myDictFile.append([[englishWords[i], ' - ', russianWords[i]]])