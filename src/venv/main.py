from PasswordGenerator import PasswordGenerator

pwGenerator = PasswordGenerator()

print("***** GENERATORE PASSWORD SICURE *****")
print("Specificare la lunghezza della password...")
pwLength = int(input())

print("Scegliere i tipi di caratteri da utilizzare per generare la password...\n"
      "[Scrivere i numeri dei tipi desiderati senza separarli.]\n"
      "[1] Lettere minuscole\n"
      "[2] Lettere maiuscole\n"
      "[3] Cifre\n"
      "[4] Caratteri speciali")
userList = False
while userList == False:
      charTypes = input()
      userList = pwGenerator.userInput(charTypes)
      if userList == False:
            print("[1] Lettere minuscole\t"
            "[2] Lettere maiuscole\t"
            "[3] Cifre\t"
            "[4] Caratteri speciali")
            
#ensureVariety chiama internamente buildCharsAvailable per costruire la lista di caratteri disponibili.
password = pwGenerator.ensureVariety(pwLength, userList) 
print(f"Password → {password}")
entropy = pwGenerator.pwStrength(password)
print(f"Entropia → {entropy}")
print(f"{pwGenerator.calcViolation(entropy)}")