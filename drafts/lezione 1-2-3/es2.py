nome = input ("Nome: ")
età = int(input("età: "))
città = input ("città: ")
email = input ("email: ")

profilo =  {
    "nome": nome,
    "età": età,
    "città": città,
    "email": email
}

print ("valori: ", profilo)
print ("la tua mail è: "profilo["email"])

