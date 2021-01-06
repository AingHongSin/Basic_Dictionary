import pandas

class DictionaryBackEnd:

    def __init__(self):

        self.data = pandas.read_csv('Resourcese/English - Khmer translation.csv')

    def finding_word(self, word) -> list:
        output = [word for word in self.data[self.data.English == word].Khmer]
        return output