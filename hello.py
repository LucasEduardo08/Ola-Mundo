from math import sqrt

# Questão 1
indice = 13
soma = k = 0

while k < indice:
    k += 1
    soma += k

print(f'Questão 1: O valor da soma é {soma}')

# Questão 2
valor = int(input("Insira um valor: "))

if int(sqrt(valor))**2 == valor:
    aux_1 = 5 * valor**2 + 4
    aux_2 = 5 * valor**2 - 4

    if int(sqrt(aux_1))**2 == (aux_1) or int(sqrt(aux_2))**2 == (aux_2):
        print("Pertence a série de fibonacci")

    else:
        print("Não pertence a série de fibonacci") 
        

else:
    print("Não pertence a série de fibonacci")

# Questão 5
string = input("Insira uma string:")

print(string[::-1])
