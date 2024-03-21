class Translator:

    def __init__(self):
        self.dizionario = {}

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
            s = f[i].split(" ")
            self.dizionario[s[0].lower()] = [s[1].lower()]

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        s = entry.split(" ")
        if self.dizionario.get(s[0].lower()) is None:
            self.dizionario[s[0].lower()] = []
        for i in range(1, len(s)):
            self.dizionario.get(s[0].lower()).append(s[i])

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        result = self.dizionario.get(query.lower())
        return result

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        i = 0
        for j in range(len(query)):
            if query[j] == "?":
                i = j
                break
        listaParole = []
        lettere = "abcdefghijklmnopqrstuvwxyz"
        for j in range(len(lettere)):
            parola = ""
            for k in range(len(query)):
                if k == i:
                    parola += lettere[j]
                else:
                    parola += query[k]
            listaParole.append(parola)
        result = []
        for p in listaParole:
            if self.handleTranslate(p) is not None:
                result += self.handleTranslate(p)
        return result

