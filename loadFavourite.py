import pandas as pd

# i need to move data from one csv to another
class FavouriteDict():
    def __init__(self, favDictPath, mainDictPath):
        self.favDictPath = favDictPath
        self.mainDictPath = mainDictPath
# TODO разберись с кодировками!!
    def loadNewWords(self):
        favPd = pd.read_csv(self.favDictPath, sep=';', header=None)
        mainPd = pd.read_csv(self.mainDictPath, sep=';')
        newDf = pd.DataFrame(list(zip(list(favPd[2]), [''] * favPd.shape[0], list(favPd[3]))),\
                             columns=['word', 'transcript', 'translate'])
        mainPd = mainPd.append(newDf, ignore_index=True)
        mainPd.to_csv(self.mainDictPath, index=False)





