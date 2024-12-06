import random

'''
    Costruisce una lista contenente i caratteri con il codice ascii compreso tra a e b
'''
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
        self.password = ""

    '''
        Costruisce la lista charsAvailable, contenente i tipi di carattere scelti dall'utente
    '''
    def buildCharsAvailable(self, choices):
        for i in choices: # Scorre una lista contenente i tipi di carattere scelti dall'utente
            if i == 1: # Lettere minuscole
                for j in self.lowercase:
                    self.charsAvailable.append(j)
            elif i == 2: # Lettere maiuscole
                for j in self.uppercase:
                    self.charsAvailable.append(j)
            elif i == 3: # Cifre
                for j in self.digits:
                    self.charsAvailable.append(j)
            elif i == 4: # Caratteri speciali
                for j in self.specialChars:
                    self.charsAvailable.append(j)
            else:
                break
        return self.charsAvailable
    
    '''
        Costruisce la password scegliendo casualmente un carattere nella lista generata da buildCharsAvailable(), 
        la scelta viene ripetuta fino a raggiungere il valore di lunghezza fornito dall'utente
    '''
    def buildPassword(self, length):
        i = 0
        while i <= length: # Ripete fino a raggiungere la lunghezza inserita dall'utente
            randomChoice = random.randint(1, len(self.charsAvailable)) # Genera un indice casuale tra 1 e la lunghezza della lista charsAvailable.
            for j in range(1, len(self.charsAvailable)): # Scorre la lista charsAvailable
                if j == randomChoice:
                    self.password += self.charsAvailable[j-1] # Aggiunge il carattere corrispondente all'indice.
            i += 1
        return self.password
