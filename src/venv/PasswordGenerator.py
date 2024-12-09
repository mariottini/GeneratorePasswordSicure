import math
from tqdm import tqdm
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

    def InputUser():
     while True:
        try:
            # Input per la lunghezza della password
            LunghezzPass = int(input("Inserire quanti caratteri deve essere lunga la password: "))

            # Input per i set di caratteri
            NumCorrispondeAllaLista = input("Quali set di caratteri vuoi che vengano utilizzati nella generazione della password?\n"
                                             "[1] lowercase\n"
                                             "[2] uppercase\n"
                                             "[3] digits\n"
                                             "[4] specialChars\n")
            
            # Trasforma l'input in una lista di numeri interi
            NumCorrispondeAllaLista = [int(c) for c in NumCorrispondeAllaLista]

            # Controllo per rimuovere duplicati e valori non validi
            NuovoArray = []
            for numero in NumCorrispondeAllaLista:
                if numero > 4 or numero < 0:
                    raise ValueError("Attenzione, inserire solamente cifre tra 0 e 4")
                if numero not in NuovoArray:
                    NuovoArray.append(numero)

            # Output dell'array di set di caratteri scelti
            print("Questo è il nuovo array con le scelte valide:")
            print(NuovoArray)
            
            # Rompi il ciclo se tutto è corretto
            break
        except ValueError as e:
            print(e)
            print("Hai inserito un input non valido! Riprova.")
        except Exception as e:
            print("Errore non previsto:", e)


    
    def HowStrongIsPw(self, Password):
        """Calcola l'entropia della password."""
        PasswordInList = list(Password)  # Converte la password in una lista di caratteri
        CalcoloEntropia = 0  # Inizializza l'entropia a zero
        #uso dei boolean che fanno in modo che appena trova un carattere di una lista non lo raggiunge di nuovo
        has_lowercase = False
        has_uppercase = False
        has_digits = False
        has_specialChars = False

        for element in PasswordInList:
            # Controlla se il carattere è in lowercase
            if element in self.lowercase and not has_lowercase:
                CalcoloEntropia += 26
                has_lowercase = True
                continue

            # Controlla se il carattere è in uppercase
            if element in self.uppercase and not has_uppercase:
                CalcoloEntropia += 26
                has_uppercase = True
                continue

            # Controlla se il carattere è un numero
            if element in self.digits and not has_digits:
                CalcoloEntropia += 10
                has_digits = True
                continue

            # Controlla se il carattere è un carattere speciale
            if element in self.specialChars and not has_specialChars:
                CalcoloEntropia += 32
                has_specialChars = True
                continue

        if CalcoloEntropia == 0:
           return 0  # Nessuna categoria soddisfatta
        print(f"CalcoloEntropia prima della moltiplicazione per lunghezza: {CalcoloEntropia}")
        # Calcola l'entropia totale
        CalcoloEntropia = math.log2(CalcoloEntropia) * len(Password)
        print(f"Entropia calcolata: {CalcoloEntropia}")
        return CalcoloEntropia
    def charsAvailableBuilder():
        return
    def display_PwBar(self, CalcoloEntropia,password):
        """Mostra una barra di caricamento basata sulla forza della password."""
        max_CalcoloEntropiaChars = 94  # Entropia massima prendendo per assurdo che la password perfetta sia lunga 16 caratteri, uso questo modo per evitare di avantaggiare le password corte
        max_CalcoloEntropia = (math.log2(max_CalcoloEntropiaChars))*16
        print("questo è il max calcolo " , max_CalcoloEntropia)
        # Calcola la percentuale di forza per poi rappresentarla fisicamente 
        strength_percentage = min(100, int((CalcoloEntropia / max_CalcoloEntropia) * 100))

        print(strength_percentage)
      
        tentativi_per_secondo = 10000
        secondi = (2**CalcoloEntropia)/tentativi_per_secondo
        minuti = secondi/60
        ore = minuti/60
        print(
        f"Numero totale di tentativi che un attacco brute force dovrebbe effettuare per avere una possibilità di successo: {int(2**CalcoloEntropia):,}")
        print(
        f"Ossia in secondi: {secondi:.2f} secondi"
)
        print(
        f"In minuti: {minuti:.2f} minuti"
)
        print(
    f"In ore: {ore:.2f} ore"
)  
        print("Livello di sicurezza password:")
        for _ in tqdm(range(strength_percentage), total=100, desc="Strength", ncols=100,mininterval=0.1):
         pass
        print("I numeri sono stati ottenuti partendo dal pressuposto che il calcolatore vada a eseguire 10000 tentativi al secondo")
    def charsAvailableBuilder():
         return
    

    


