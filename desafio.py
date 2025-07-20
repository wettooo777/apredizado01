frase = (input("Digite qualquer coisa: "))
algarismos = '1234567890'
frase = frase.lower()
contador = 0

for letra in frase:
    if letra in algarismos:
        contador += 1

print(f"A frase tem {contador} algarismos.")


