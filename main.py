import translator as tr


def stringaTraduzioni(lista):
    stringa = ""
    for i in range(len(lista)):
        stringa += lista[i]
        if i != len(lista) - 1:
            stringa += ", "
    return stringa


t = tr.Translator()

flag = True

while flag:

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        t.handleAdd(input("Ok, quale parola devo aggiungere?\n"))
    if int(txtIn) == 2:
        result = t.handleTranslate(input("Ok, quale parola devo cercare?\n"))
        print(stringaTraduzioni(result))
    if int(txtIn) == 3:
        result = t.handleWildCard(input("Ok, quale parola devo cercare?\n"))
        print(stringaTraduzioni(result))
    if int(txtIn) == 4:
        for e in t.dizionario:
            print(e + " " + stringaTraduzioni(t.dizionario[e]))
    if int(txtIn) == 5:
        flag = False
