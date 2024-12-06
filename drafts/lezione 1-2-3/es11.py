n = ''
lista_numeri = []
numeri = int(input("num max numeri: ")) #chiedo quanti numeri voglio in lista

while n is not int:
    try:
        for i in range (numeri):   
            n = int(input("Inserisci numero positivo: "))
            lista_numeri.append(n)
        break
    except ValueError:
        print ("valore errrato, riprova") 

while n < 0:
    print ("numero negativo, riprova")
    int(input("Inserisci numero positivo: "))
    lista_numeri.append(n)

lista_numeri_copia = lista_numeri[:]
lista_numeri_copia.sort ()

if lista_numeri == lista_numeri_copia:
    print ("lista ordinata")
else:
    print ("lista non ordinata")


