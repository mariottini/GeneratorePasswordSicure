import random
import math

class PasswordGenerator:
    def __init__(self):
        # a-z
        self.lowercase = [chr(i) for i in range(97, 123)]
        # A-Z
        self.uppercase = [chr(i) for i in range(65, 91)]
        # 0-9
        self.digits = [chr(i) for i in range(48, 58)]
        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        self.specialChars = [chr(i) for i in range(33, 48)] + \
                            [chr(i) for i in range(58, 65)] + \
                            [chr(i) for i in range(91, 97)] + \
                            [chr(i) for i in range(123, 127)]
        self.charsAvailable = []
        self.password = ""

    '''
        Costruisce la lista charsAvailable, contenente i tipi di carattere scelti dall'utente
    '''
    def buildCharsAvailable(self, choices):
        self.charsAvailable = []
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
    def buildPassword(self, length, charsAvailable):
        self.password = ""
        i = 0
        while i < length: # Ripete fino a raggiungere la lunghezza inserita dall'utente
            randomChoice = random.randint(0, len(charsAvailable)-1) # Genera un indice casuale tra 0 e la lunghezza della lista charsAvailable-1.
            for j in range(0, len(charsAvailable)): # Scorre la lista charsAvailable
                if j == randomChoice:
                    self.password += charsAvailable[j] # Aggiunge il carattere corrispondente all'indice.
            i += 1
        return self.password

    '''
        Converte l'input dell'utente per la scelta dei set di caratteri in una lista di interi    
    '''
    def userInput(self, charTypes):
        # while True:
            try:
                # Trasforma l'input in una lista di numeri interi
                charTypes = [int(c) for c in charTypes]

                # Inserisce in una nuova lista solo i numeri validi, senza duplicati
                newList = []
                for n in charTypes:
                    if n > 4 or n < 1:
                        raise ValueError
                    if n not in newList:
                        newList.append(n)

                return newList
            
            except ValueError:
                print("Input non valido! Inserire solo numeri tra 1 e 4.")
                return False
            except Exception:
                print("Errore sconosciuto.")
                return False

    '''
        Calcola l'entropia della password generata.
        [Entropia → Misurazione in bit dell'imprevedibilità di una password]
    '''
    def pwStrength(self, password):
        entropy = 0  # Inizializza l'entropia a zero
        pwToList = list(password)  # Converte la password in una lista di caratteri
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
    
    '''
        Calcola numero di tentativi e tempo necessari per violare la password generata
    '''
    def calcViolation(self, entropy):
        tries = 2**entropy # Numero massimo di tentativi per violare la password
        triesPerSec = 10**9 # Numero indicativo di tentativi al secondo compiuti dal PC attaccante
        # Tempo necessari per violare la password in secondi, minuti, ore
        seconds = tries/triesPerSec
        minutes = seconds/60
        hours = minutes/60
        days = hours/24
        months = days/30
        years = days/365
        centuries = years/100
        millennia = years/1000

        if millennia > 1:
            time = f"più di un millennio"
        elif millennia == 1:
            time = f"{millennia:.0f} millenni"
        elif centuries >= 1:
            time = f"{centuries:.0f} secoli"
        elif years >= 1:
            time = f"{years:.0f} anni" 
        elif months >= 1:
            time = f"{months:.0f} mesi"
        elif days >= 1: 
            time = f"{days:.0f} giorni" 
        elif hours >= 1: 
            time = f"{hours:.0f} ore" 
        elif minutes >= 1: 
            time = f"{minutes:.0f} minuti" 
        else: 
            time = f"{seconds:.5f} secondi"

        if tries > 999999:
            printTries = "anche più di un miliardo di"
        else:
            printTries = f"{tries:.0f}"

        return f"Se un PC eseguisse un attacco brute force, per violare la password potrebbe effettuare {printTries} tentativi.\n" \
                f"Se il PC eseguisse l'attacco ad una velcoità di 10^{int(math.log10(triesPerSec))} tentativi al secondo, ci impiegherebbe {time}"
    

    def dictionary(self):
        with open ('dictionary.txt') as file:
            content = file.read()
            words = content.split()
        return words
    
    def Password_Safety (self,password):
        password_alpha = ''.join([char for char in password if char.isalpha()])
        pw_lower = password_alpha.lower()
        word_list = self.dictionary()
        word_saver = []
        for i in range (len(word_list)):
            if word_list[i].startswith(pw_lower[0]) and len(word_list[i]) == len(pw_lower):  
                word_saver.append(word_list[i])
                #print (word_saver)
                
        for i in range (len(word_saver)):
            if pw_lower ==  word_saver[i]:
                return (f"Parola {word_saver[i]} trovata, password non sicura")
        return ("Password sicura, nessuna parola trovata") 