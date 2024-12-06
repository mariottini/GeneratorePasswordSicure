while True:
    a = int(input("numero 1: "))
    b = int(input("numero 2: "))
    operazione = input("operazione (1 = somma, 2 = sottr, 3 = molt, 4 = div) oppure digita fine:  ")

    if operazione == "fine":
        print("programma terminato")
        break  

    if operazione == 1:
        ris = a+b
        print(ris)
    elif operazione == 2:
        ris = a-b
        print(ris)
    elif operazione == 3:
        ris = a*b
        print(ris)
    elif operazione == 4:
        try:
            ris = a/b
            print(ris)
        except ZeroDivisionError:
            print("Operazione impossibile")

