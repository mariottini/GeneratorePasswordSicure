def pwPower(passowrd):

    passwordList = list(password)

    # Potenza iniziale
    power = 0

    # Aggiungi potenza in base alla lunghezza
    power += len(passwordList)

    if len(passwordList) <= 4:
        lenght = "molto breve"
    elif len(passwordList) in range(5,7):
        lenght = "breve"
    elif len(passwordList) in range(8,15):
        lenght = "nella norma"
    elif len(passwordList) >= 16:
        lenght = "ottimale"

    # Aggiungi potenza proporzionalmente ai tipi di caratteri
    pow = 0
    if self.lowercase in passwordList:
        pow += 1
    if self.uppercase in passwordList:
        pow += 1
    if self.digits in passwordList:
        pow += 1
    if self.specialChars in passwordList:
        pow += 1

    if pow in range(1,2):
        comp = "minima"
    elif pow == 3:
        comp = "standard"
    elif pow == 4:
        comp = "efficacie"

    power += (2**pow)

    # Sottrai potenza in base ai doppioni
    i = 0
    while i < len(passwordList):
        if passwordList[i] in passwordList[(i+1):-1]:
            power -= 1
            print("-1")
        else:
            power += 0
            print("+1")
        i += 1

    # Sottrai potenza se la password contiene una parola conosciuta o molto usata

    if "ciao" in password:
        power -= 16
        used = True

    print(power)

    # Print del risultato al utente
    if power <= 16:
        print("La passowrd generata è poco potente, prova nuovamente")
    elif power in range(17,30):
        print("La password è buona, ma non ottimale")
    elif power > 30:
        print("La password generata è ottimale")

    print(f"La password ha una lunghezza {lenght} e una complessità {comp}")
    if used == True:
        print("La password contiene una parola molto usata")





