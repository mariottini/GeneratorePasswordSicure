nome1 = input ("nome membro 1: ") 
età1 = int(input ("età membro 1: "))
città1 = input ("città membro 1: ")
genere1 = input ("preferenza genere membro 1: ") 

nome2 = input ("nome membro 2: ") 
età2 = int (input ("età membro 2: ")) 
città2 = input ("città membro 2: ") 
genere2 = input ("preferenza genere membro 2: ")

membro1 = {
    "titolo": nome1,
    "autore": età1,
    "anno": città1,
    "genere": genere1
}

membro2 = {
    "titolo": nome2,
    "autore": età2,
    "anno": città2,
    "genere": genere2
}

lista_membri = (nome1,nome2)

titolo1 = input ("titolo primo libro m1: ") 
autore1 = input ("autore libro m1: ") 
anno1 = int(input ("anno del libro m1: ")) 
generel1 = input ("genere libro m1: ") 

titolo2 = input ("titolo secondo libro m1: ") 
autore2 = input ("autore libro m1: ") 
anno2 = int(input ("anno del libro m1: ")) 
generel2 = input ("genere libro m1: ") 

libro1 = {
    "titolo": titolo1,
    "autore": autore1,
    "anno": anno1,
    "genere": generel1
}

libro2 = {
    "titolo": titolo2,
    "autore": autore2,
    "anno": anno2,
    "genere": generel2
}

titolo3 = input ("titolo primo libro m2: ") 
autore3 = input ("autore libro m2: ") 
anno3 = int(input ("anno del libro m2: ")) 
genere3 = input ("genere libro m2: ") 

titolo4 = input ("titolo secondo libro m2: ") 
autore4 = input ("autore libro m2: ") 
anno4 = int(input ("anno del libro m2: ")) 
genere4 = input ("genere libro m2: ") 

libro3 = {
    "titolo": titolo3,
    "autore": autore3,
    "anno": anno3,
    "genere": genere3
}

libro4 = {
    "titolo": titolo4,
    "autore": autore4,
    "anno": anno4,
    "genere": genere4
}


libri_m1 = (libro1,libro2)
libri_m2 = (libro4,libro4)
allgeneri = (genere1,genere2,generel1,generel2,genere3,genere4)

print ("Lista membri: ",lista_membri)
print ("primo libro inserito: ",libro1)
print ("generi: ", allgeneri)



