from random import random 

numero = int(input("numero: "))
def rand (num):
    num = random.randint(1,100)
    while numero != num : 
        numero = int(input("numero errato")) 
    if numero == num:
        print ("hai indovinato") 

    nim = rand (num)



