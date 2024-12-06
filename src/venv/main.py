from PasswordGenerator import PasswordGenerator
import random

pwGenerator = PasswordGenerator()
# print(f"lowercase: {pwGenerator.lowercase} \n"
    #   f"uppercase: {pwGenerator.uppercase} \n"
    #   f"digits: {pwGenerator.digits} \n"
    #   f"special chars: {pwGenerator.specialChars}")

# print(f"random lowercase char:\n {random.choice(pwGenerator.lowercase)}")    
# print(f"5 random lowercase chars:\n {random.choices(pwGenerator.lowercase, k=5)}") 

print("PASSWORD GENERATOR")
lunghezzaPW = input("Quanto deve essere lunga la password? ")
print("Quali set di caratteri vuoi che vengano utilizzati nellagenerazione della password?\n"
      "[1] lowercase\n"
      "[2] uppercase\n"
      "[3] digits\n"
      "[4] specialChars\n")
scelta=input()

print(scelta)


