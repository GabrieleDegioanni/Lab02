class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, entry):
        s = entry.split(" ")
        if self.dizionario.get(s[0].lower()) is None:
            self.dizionario[s[0].lower()] = []
        for i in range(1, len(s)):
            self.dizionario.get(s[0].lower()).append(s[i])

    def translate(self, query):
        result = self.dizionario.get(query.lower())
        return result

    def translateWordWildCard(self, query):
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
            if self.translate(p) is not None:
                result += self.translate(p)
        return result

    def stringaTraduzioni(self, lista):
        stringa = ""
        for i in range(len(lista)):
            stringa += lista[i]
            if i != len(lista) - 1:
                stringa += ", "
        return stringa

    def stringa_elemento(self, query):
        return f"{query} Traduzioni: {self.stringaTraduzioni(self.translate(query))}"

    def stringa_dizionario(self):
        result = ""
        for k in self.dizionario.keys():
            result += self.stringa_elemento(k) + "\n"
        return result

