from random import random 
import string
from PasswordGenerator import lista_caratteri 
i = 0 

lista1 = list(string.ascii_lowercase)
lista2 = list(string.ascii_uppercase)
lista3 = list(string.digits)
lista4 = list(string.punctuation)

listaspecifica = int(input("quante liste vuoi aggiungere?: "))
while listaspecifica > 4:
      listaspecfica = int(input("numero massimo superato, riprova: "))
while i < listaspecifica:
         n = int(input(f"numero {i+1}: "))
         i = i+1
         valori = lista_caratteri (lista1,lista2,lista3,lista4,n)
         print (valori)




