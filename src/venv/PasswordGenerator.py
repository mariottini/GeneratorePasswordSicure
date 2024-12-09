import math
# from tqdm import tqdm

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

    def userInput(charTypes):
        while True:
            try:
                # Trasforma l'input in una lista di numeri interi
                charTypes = [int(c) for c in charTypes]

                # Inserisce in una nuova lista solo i numeri validi, senza duplicati
                newArray = []
                for n in charTypes:
                    if n > 4 or n < 1:
                        raise ValueError
                    if n not in newArray:
                        newArray.append(n)

                return newArray
            
            except ValueError:
                print("Input non valido! Inserire solo numeri tra 1 e 4.")
            except Exception:
                print("Errore sconosciuto.")

    def pwStrength(self, password):
        """Calcola l'entropia della password."""
        pwToList = list(password)  # Converte la password in una lista di caratteri
        entropy = 0  # Inizializza l'entropia a zero
        # Inizializzazione booleani per aggiornare la variante dei carateri solamente una volta per ogni set di caratteri
        hasLowercase = False
        hasUppercase = False
        hasDigits = False
        hasSpecialChars = False

        try:    
            for element in pwToList:
                # Controlla se il carattere è in lowercase
                if element in self.lowercase and not hasLowercase:
                    entropy += 26
                    hasLowercase = True
                    continue

                # Controlla se il carattere è in uppercase
                elif element in self.uppercase and not hasUppercase:
                    entropy += 26
                    hasUppercase = True
                    continue

                # Controlla se il carattere è un numero
                elif element in self.digits and not hasDigits:
                    entropy += 10
                    hasDigits = True
                    continue

                # Controlla se il carattere è un carattere speciale
                elif element in self.specialChars and not hasSpecialChars:
                    entropy += 32
                    hasSpecialChars = True
                    continue

                if entropy <= 0: 
                    raise ValueError
                
        except ValueError:
            return "La variante dei caratteri utilizzati nella password è inferiore o uguale a 0"
        
        # Calcola l'entropia totale
        entropy = math.log2(entropy) * len(password)
        return entropy
    
    def calcViolation(entropy):
        tries = 2**entropy # Numero massimo di tentativi per violare la password
        triesPerSec = 10000 # Numero indicativo di tentativi al secondo compiuti dal PC attaccante
        # Tempo necessari per violare la password in secondi, minuti, ore
        seconds = tries/triesPerSec
        # minutes = seconds/60
        # hours = minutes/60

        i = 0
        while i < seconds:
            if seconds > 59:
                minutes += 1
                seconds = 0

            if minutes > 59:
                hours += 1
                minutes = 0

            i += 60

        return f"Se un PC esegue un attacco brute force, per violare la password effettuerà un massimo di {tries} tentativi. Se il PC esegue l'attacco ad una velcoità di {triesPerSec} tentativi al secondo, ci impiegherà {hours} ore, {minutes} minuti, {seconds} secondi."