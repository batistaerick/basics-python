# 1) Escreva um algoritmo que solicite um limite inteiro como entrada e que apresente na tela
# os  termos  das  séries  abaixo  menores  ou  iguais  ao  limite  informado.  O  algoritmo  deve
# apresentar também a soma de todos os termos apresentados em cada série.
# a) 3, 6, 9, 12, 15, 18, 21...
# b) 5, 10, 15, 20, 25, 30...
# c) 1, 2, 4, 8, 16, 32, 64...
# d) 1, 8, 27, 64, 125, 216...(1^3, 2^3, 3^3, 4^3, 5^3, 6^3, ...)

limite = int(input('Digite um numero: '))

lista = []

aux = 3
while aux <= limite:
    lista.append(aux)
    aux += 3

aux = sum(lista)
print('\nOs termos A sao {} e a soma e: {}' .format(lista, aux))

aux = 5
lista = []
while aux <= limite:
    lista.append(aux)
    aux += 5

aux = sum(lista)
print('\nOs termos B sao {} e a soma e: {}' .format(lista, aux))

aux = 1
lista = []
while aux <= limite:
    lista.append(aux)
    aux = aux * 2

aux = sum(lista)
print('\nOs termos C sao {} e a soma e: {}' .format(lista, aux))

aux = 1
cont = 1
lista = []
while cont <= limite:
    lista.append(aux)
    cont += 1
    aux = cont ** 3

aux = sum(lista)
print('\nOs termos D sao {} e a soma e: {}' .format(lista, aux))


# 2) A série de Fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... Começa  com  os  termos  0  e  1
# e  tem  a  propriedade  de  que  cada  temo  subsequente equivale à soma dos dois termos
# anteriores. Escreva um algoritmo que leia um limite a partir  do  teclado  e  que
# apresente  na  tela  os  temos  da  série  de  Fibonacci  menores  ou iguais ao limite
# informado.  O  algoritmo  também  deve  apresentar  a  soma  dos  termos gerados.

limite = int(input("\nInforme um numero: "))
a = 0
b = 1
soma = 1

print(f'{a} {b}', end=' ')

for i in range(limite):
    novo = a + b
    print(novo, end=' ')
    if novo >= limite:
        break
    a = b
    b = novo
    soma = soma + novo

print("\nA soma e:", soma)
