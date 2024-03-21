import dictionary

class Translator:

    def __init__(self):
        self.dizionario = dictionary.Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("------------------------------\nTranslator Alien-Italian\n------------------------------\n1. Aggiungi una nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit\n------------------------------\n")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        f = open(dict, "r").read().splitlines()
        for i in range(0, len(f)):
            self.dizionario.addWord(f[i])

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        self.dizionario.addWord(entry)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self.dizionario.translate(query)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)

    def stampa_dizionario(self):
        return self.dizionario.stringa_dizionario()
