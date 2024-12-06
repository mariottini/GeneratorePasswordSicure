i = 0 
nmin = 9999
nmax = 0
numeri = int(input("num max numeri: ")) #chiedo quanti numeri voglio in lista
lista = []

for i in range (numeri):
 n = int (input(f"Inserisci numero {i+1}: ")) 
 lista.append(n)

def numax (nmax): 
  for n in lista:  
    if n > nmax:  #trovo il valore massimo (con nmax = 0)
      nmax = n

def numin (nmin):
  for n in lista:
    if n < nmin: #trovo il valore minimo (con nmin = 9999)
      nmin = n

def media ():
    return sum(lista) / len(lista) #per la media uso la somma della lista diviso la lunghezza della lista


numax(nmax) #richiamo le funzioni
numin(nmin)
nmedia = media() #su suggerimento di chatgpt

print ("numero max è:", nmax, "numero min è:",nmin, "la media è", nmedia)

