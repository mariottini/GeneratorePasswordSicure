from PasswordGenerator import PasswordGenerator
import random

pwGenerator = PasswordGenerator()
# print(f"lowercase: {pwGenerator.lowercase} \n"
    #   f"uppercase: {pwGenerator.uppercase} \n"
    #   f"digits: {pwGenerator.digits} \n"
    #   f"special chars: {pwGenerator.specialChars}")

# print(f"random lowercase char:\n {random.choice(pwGenerator.lowercase)}")    
# print(f"5 random lowercase chars:\n {random.choices(pwGenerator.lowercase, k=5)}") 


while True:
    try:
     LunghezzPass = int(input("Inserire quanti caratteri deve essere lunga la password: "))
     NumCorrispondeAllaLista = input("Quali set di caratteri vuoi che vengano utilizzati nellagenerazione della password?\n"
      "[1] lowercase\n"
      "[2] uppercase\n"
      "[3] digits\n"
      "[4] specialChars\n")
     NumCorrispondeAllaLista = list(NumCorrispondeAllaLista)
     i=0
     NumProv = []
     NuovoArray = []
     while i < len(NumCorrispondeAllaLista):
         numeroCost = int(NumCorrispondeAllaLista[i])
         NumProv.append(numeroCost)
         if(NumProv[i]>4 or NumProv[i]<0):
             raise ValueError("Attenzione, inserire solamente cifre sotto il 5")
         if(NumProv[i] not in NuovoArray):
            NuovoArray.append(NumProv[i])
         i = i + 1
     print("questo è il nuovo array")
     print(NuovoArray)
    except (ValueError, Exception):
       print("No attento, hai inserito un input non valido!, riprova")
       
    else: 
          break
