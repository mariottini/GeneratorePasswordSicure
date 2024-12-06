import random

def lista_caratteri (lista1,lista2,lista3,lista4,n):
    valori_lista = []

    if n == 1: #se l'utente ha inserito 1 e il numero random è 1
        valori_lista.append(lista1) #aggiungo i valori alla lista da scegliere
    elif n == 2:
        valori_lista.append(lista2)
    elif n == 3:
        valori_lista.append(lista3)
    elif n == 4:
        valori_lista.append(lista4)

    return valori_lista
            
        





    