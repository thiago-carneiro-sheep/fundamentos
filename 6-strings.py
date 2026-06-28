movieName = "Interstellar"
movieName2 = "interstellar"


print(movieName ==  movieName2)  # False, because of case sensitivity

moviedescription = """
                    Interstellar é um filme de ficção científica
                    dirigido por Christopher Nolan, lançado em 2014. 
                    O filme explora temas como viagem no tempo"""

print(moviedescription)

#MULTIPLICADOR DE STRINGS
print((movieName + "\n") * 3)  # InterstellarInterstellarInterstellar

#procurando por uma substring dentro de uma string  
print("Interstellar" in moviedescription)  # True
print("interstellar"  in moviedescription)  # False