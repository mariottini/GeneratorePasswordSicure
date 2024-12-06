titolo1 = input ("titolo libro: ") 
autore1 = input ("autore libro: ") 
anno1 = int(input ("anno del libro: ")) 
genere1 = input ("genere libro: ") 

titolo2 = input ("titolo libro: ") 
autore2 = input ("autore libro: ") 
anno2 = int(input ("anno del libro: ")) 
genere2 = input ("genere libro: ") 

libro1 = {
    "titolo": titolo1,
    "autore": autore1,
    "anno": anno1,
    "genere": genere1
}

libro2 = {
    "titolo": titolo2,
    "autore": autore2,
    "anno": anno2,
    "genere": genere2
}

catalogo = (libro1,libro2)

print ("catalogo libreria: ", catalogo)
print ("libro 2: ", catalogo[1])
print ("esempio", genere2)

