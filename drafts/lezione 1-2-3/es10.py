n = ''

while n is not int:
    try:
        n = int(input('inserisci numero positivo: '))
        break
    except ValueError:
        print('Valore errato, riprova')

while n < 0:
        print ("numero negativo, riprova")
        n = int(input("inserisci numero positivo: "))

def conto (n):
    i = 0
    while i <= n:
           nrov = n-i
           i = i+1
           print (nrov)

print ("conto alla rovescia: ")
rovescio = conto(n)


