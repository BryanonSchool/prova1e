print ("Lorenzo Cristianini de Oliveira")
print ("Prova de Introdução a Programação")
from random import randint
n = randint(1, 100)
while (g := int(input("Tente adivinhar: "))) != n:
    print("Maior" if g < n else "Menor")
print("Acertou!")