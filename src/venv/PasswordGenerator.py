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
        self.complexity = 0
        self.entropy = 0
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
        Calcola la complessità secondo una serie di parametri:
        - Lunghezza della password
        - Varieta dei set di caratteri
        - Presenza di parole riconoscibili del vocabolario italiano
        - Presenza di pattern di caratteri ripetuti o crescenti
    '''
    def pwComplexity(self, password):
        self.complexity = 0  # Inizializza la complessità a zero
        '''Lunghezza'''
        for i in range(2, 7):
            if len(password) >= 2**i:
                self.complexity += 2**i
        
        '''Varietà'''
        hasLowercase = any(c in self.lowercase for c in self.password)
        hasUppercase = any(c in self.uppercase for c in self.password)
        hasDigits = any(c in self.digits for c in self.password)
        hasSpecialChars = any(c in self.specialChars for c in self.password)

        if hasLowercase:
            self.complexity += len(self.lowercase)
        if hasUppercase:
            self.complexity += len(self.uppercase)
        if hasDigits:
            self.complexity += len(self.digits)
        if hasSpecialChars:
            self.complexity += len(self.specialChars)

        '''Vocabolario''' # Not finished...
        # with open ("src/assets/dictionaryIT.txt") as file:
        #     content = file.read()
        #     wordList = content.split()

        # passwordAlpha = ''.join([char for char in password if char.isalpha()])
        # pwLower = passwordAlpha.lower()
        # wordSaver = []
        # for i in range (len(wordList)):
        #     if wordList[i].startswith(pwLower[0]) and len(wordList[i]) == len(pwLower):  
        #         wordSaver.append(wordList[i])
                
        # for i in range (len(wordSaver)):
        #     if pwLower ==  wordSaver[i]:
        #         self.complexity -= len(wordSaver[i])


        '''Pattern'''
        # Converto la password in una lista per iterarla
        password = list(password)
        # Liste temporanee per caratteri ripetuti e sequenze (crescenti/decrescenti)
        repeatedChar = []
        sequenceChar = []
        sequenceReverse = []
        # Contatore per caratteri ripetuti consecutivi e dizionario per riepilogo ripetizioni
        count = 0
        dictRepetion={}
        # Lista definitiva per tutte le sequenze trovate
        sequenceCharDef = []
        
        # Itero attraverso i caratteri della password
        for i in range(len(password)):
            # Controllo caratteri consecutivi uguali
            if(i< len(password)-1 and password[i] == password[i+1]):
                repeatedChar.append(password[i])
                count = count + 1 # Incremento il contatore delle ripetizioni
            elif count >= 1:
                # Se il contatore è > 1, registro il carattere nel dizionario
                if(password[i] in dictRepetion):
                    dictRepetion[password[i]] += count
                else:
                    dictRepetion[password[i]] = count
                count = 0 # Resetto il contatore

            # Controllo sequenze crescenti (basate sui valori ASCII)
            if i< len(password)-1 and ord(password[i])+1 == ord(password[i+1]):
                
                # Aggiungo il carattere alla sequenza crescente se non già presente
                if not sequenceChar or sequenceChar[-1] != ord(password[i]):
                    sequenceChar.append(ord(password[i]))
                sequenceChar.append(ord(password[i+1]))
                
            else:
                if len(sequenceChar)>2:
                    # Se la sequenza crescente è valida (almeno 2 elementi), la riconverto in caratteri normali e poi la salvo
                    sequenceChar = [chr(element) for element in sequenceChar]
                    sequenceCharDef.append(sequenceChar) 
                sequenceChar = [] # Resetto la sequenza crescente per poterla usare nuovamente in futuro
        
            # stesso processo ma stavolta per salvare le sequenze decrescenti
            if i < len(password) - 1 and ord(password[i]) - 1 == ord(password[i + 1]):
                if not sequenceReverse or sequenceReverse[-1] != ord(password[i]):
                    sequenceReverse.append(ord(password[i]))
                sequenceReverse.append(ord(password[i + 1]))
                    
            else:
                if len(sequenceReverse) > 2:
                    sequenceReverse = [chr(element) for element in sequenceReverse]
                    sequenceCharDef.append(sequenceReverse)
                sequenceReverse = []

        for key,value in dictRepetion.items():
            print(f"Carattere ripetuto → {key} (x{value})")

        for sequence in sequenceCharDef:
            print(f"Sequenza crescente/decrescente → {sequence}")
        
        # Penalizza per le ripetizioni
        for n in dictRepetion.values():
            self.complexity -= (n + 1)  # Penalità per le ripetizioni
         # Penalizza per le sequenze di caratteri
        for sequence in sequenceCharDef:
            self.complexity -= len(sequence)  # Penalità per la lunghezza delle sequenze

        return self.complexity



    '''
        Calcola l'entropia della password generata.
        [Entropia → Misurazione in bit dell'imprevedibilità di una password]
    '''
    def pwStrength(self, password):
        self.entropy = 0  # Inizializza l'entropia a zero
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
                    self.entropy += 26
                    hasLowercase = True
                    continue

                # Controlla se il carattere è in uppercase
                elif element in self.uppercase and not hasUppercase:
                    self.entropy += 26
                    hasUppercase = True
                    continue

                # Controlla se il carattere è un numero
                elif element in self.digits and not hasDigits:
                    self.entropy += 10
                    hasDigits = True
                    continue

                # Controlla se il carattere è un carattere speciale
                elif element in self.specialChars and not hasSpecialChars:
                    self.entropy += 32
                    hasSpecialChars = True
                    continue

                if self.entropy <= 0: 
                    raise ValueError
                
        except ValueError:
            return "La variante dei caratteri utilizzati nella password è inferiore o uguale a 0"
        
        # Calcola l'entropia totale
        self.entropy = math.log2(self.entropy) * len(password)
        return self.entropy
    
    '''
        Calcola numero di tentativi e tempo necessari per violare la password generata
    '''
    def calcViolation(self):
        tries = 2**self.entropy # Numero massimo di tentativi per violare la password
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