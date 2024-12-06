def buildString(list, a, b):
    for i in range(a, b):
        list.append(chr(i))
    return list

class PasswordGenerator:
    def __init__(self):
        # a-z
        self.lowercase = buildString([], 97, 123)
        # A-Z
        self.uppercase = buildString([], 65, 91)
        # 0-9
        self.digits = buildString([], 48, 58)
        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        self.specialChars = buildString([], 33, 48) + \
                            buildString([], 58, 65) + \
                            buildString([], 91, 97) + \
                            buildString([], 123, 127)
        self.charsAvailable = []

    def generatePw(self): #funzione che genera password
        pass

    def charsAvailableBuilder():
        return

'''
    BLOCCO1
        dati dall'utente -> numero caratteri pw & liste di caratteri da usare

    BLOCCO2
        in charsAvailable inserisci liste di caratteri da usare
        programma sceglie da charsAvailable un carattere random -> tante volte quanto è la lunghezza della pw
        return pw

'''
