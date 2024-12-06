from PasswordGenerator import PasswordGenerator
import random


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
charTypes = input()

pwGenerator.buildCharsAvailable([1,2,3,4]) # Supponiamo charTypes = [1,2,3,4]
print(pwGenerator.buildPassword(pwLength))
