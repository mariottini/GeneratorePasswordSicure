numero = ''
while numero is not int:
    try:
        numero = int(input('inserisci numero positivo: '))
        break
    except ValueError:
        print('Valore errato, riprova')
    if numero > 100 & numero < 1:
        print ("errore, riprova")

num =  int(input("Inserisci numero: "))
if numero == num:
    print ("hai indovinato") 

while num != numero: 
    if num > numero: 
            num = int(input("numero troppo grande: ")) 
    else:
            num = int(input("numero troppo piccolo: "))   
 

