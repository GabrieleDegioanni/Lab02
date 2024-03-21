import translator as tr

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
        print(t.stringaTraduzioni(result))
    if int(txtIn) == 3:
        result = t.handleWildCard(input("Ok, quale parola devo cercare?\n"))
        print(t.stringaTraduzioni(result))
    if int(txtIn) == 4:
        print(t.stampa_dizionario())
    if int(txtIn) == 5:
        flag = False
