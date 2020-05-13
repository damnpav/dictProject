from googletrans import Translator


class NewWord():
    def __init__(self, new_word):
        self.newWord = new_word
        self.original_word =''

    def translation(self):
        translator = Translator()
        self.original_word = translator.translate(text=self.newWord, dest='ru').text
        return self.original_word
