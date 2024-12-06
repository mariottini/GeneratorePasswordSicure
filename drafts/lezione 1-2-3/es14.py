i = 0 
num_prodotti = int(input("quanti prodotti vuoi ordinare?: ")) #chiedo quanti numeri voglio in lista
lista_numeri = []  #su suggerimento di chatgpt

def lista_spesa():
  global lista #su suggerimento di chatgpt
  for i in range (num_prodotti): 
   prodotti = int(input(f"inserisci prodotto n.{i+1}: ")) #chiedo un numero fino al massimo imposto sopra
   lista_numeri.append(prodotti) 
    
def lista_spesa_num (): 
  global nmax #su suggerimento di chatgpt
  for n in lista_numeri:  
    if n > nmax:  #trovo il valore massimo (con nmax = 0)
      nmax = n

def numin ():
  global nmin #su suggerimento di chatgpt
  for n in lista_numeri:
    if n < nmin: #trovo il valore minimo (con nmin = 9999)
      nmin = n

def media ():
    return sum(lista_numeri) / len(lista_numeri) #per la media uso la somma della lista diviso la lunghezza della lista


lista()
numax() #richiamo le funzioni
numin()
nmedia = media() #su suggerimento di chatgpt

print ("numero max è:", nmax, "numero min è:",nmin, "la media è", nmedia)