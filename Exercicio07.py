import math

# 1) Execute o  trecho de  código  abaixo.  Em  seguida, escreva  sobre  a  saída  retornada  como resposta.

lista = [1, 67.2, True, "Ana Conda"]
print("Lista Completa:", lista)
lista.remove(True)
print("Lista foi removido o valor True, logo 1 é igual True:", lista)
lista.remove(True)
print("Novamente removido o valor True, Logo o True foi removido:", lista)

# 2) Escreva um algoritmo que leia números informados pelo usuário a partir do teclado. Os
# números  devem  ser  inseridos  em  uma  lista  chamada  lista_original.  O  usuário  deve
# informar  quantos  números  ele  desejar.  Após  ler  todos  os  números  informados  pelo
# usuário,  o  algoritmo  deve  copiar  os  valores  ímpares  da  lista_original  para  uma  lista
# chamada lista_impares e também copiar os valores pares da lista_original para uma lista
# chamada lista_pares. Todas as listas devem ser apresentadas na tela.

lista_original = []
lista_pares = []
lista_impares = []
numeros = int(input('\nQuantos numeros vai digitar? '))

for i in range(numeros):
    numero = int(input('Digite o numero: '))
    lista_original.insert(i, numero)
    if numero % 2 == 0:
        lista_pares.insert(i, numero)
    else:
        lista_impares.insert(i, numero)

print('\nLista Original: ', lista_original)
print('Lista Par: ', lista_pares)
print('Lista Impar: ', lista_impares)

# 3) Escreva um algoritmo que leia duas listas de valores informados pelo usuário a partir do
# teclado.  O  algoritmo  deve  gerar  uma  nova  lista  que  seja  a  união  das  duas  listas
# informadas pelo usuário. Assim, a nova lista deve conter todos os valores presentes nas
# duas listas lidas a partir do teclado. A nova lista não deve conter valores repetidos. Todas
# as listas devem ser apresentadas na tela.

lista_1 = []
lista_2 = []

numeros = int(input('\nQuantos numeros vai digitar na Primeira lista? '))
for i in range(numeros):
    lista_1.insert(i, int(input('Digite o numero: ')))

numeros = int(input('\nQuantos numeros vai digitar na Segunda lista? '))
for i in range(numeros):
    lista_2.insert(i, int(input('Digite o numero: ')))

uniao = set(lista_1 + lista_2)

print('Primeira lista: ', lista_1)
print('Segunda lista: ', lista_2)
print('Uniao das listas: ', uniao)

# 4) Escreva um algoritmo que leia duas listas de valores informados pelo usuário a partir do
# teclado.  O  algoritmo  deve  gerar  uma  nova  lista  que  seja  a  interseção  das  duas  listas
# informadas  pelo  usuário.  Assim,  a  nova  lista  deve  conter  apenas  os  valores  comuns  às
# duas listas lidas a partir do teclado. A nova lista não deve conter valores repetidos. Todas
# as listas devem ser apresentadas na tela.

lista_1 = []
lista_2 = []
intersecao = set()

numeros = int(input('\nQuantos numeros vai digitar na Primeira lista? '))
for i in range(numeros):
    lista_1.insert(i, int(input('Digite o numero: ')))

numeros = int(input('\nQuantos numeros vai digitar na Segunda lista? '))
for i in range(numeros):
    lista_2.insert(i, int(input('Digite o numero: ')))

for i in range(len(lista_2)):
    for j in range(len(lista_1)):
        if lista_1[j] == lista_2[i]:
            intersecao.add(lista_1[j])

print(intersecao)

# 5) Escreva um algoritmo que leia números informados pelo usuário a partir do teclado. Os
# números devem ser inseridos em uma lista. O usuário deve  informar quantos números
# ele  desejar.  Após  ler  todos  os  números  informados  pelo  usuário,  o  algoritmo  deve
# apresentar na tela:
# a) A média aritmética dos números informados.
# b) O desvio padrão em relação à média aritmética dos números informados.

lista = []
lista_auxiliar = []
desvio_padrao = 0
media = 0

numeros = int(input('\nQuantos numeros vai digitar na lista? '))
for i in range(numeros):
    lista.insert(i, float(input('Digite o numero: ')))
    media += lista[i]

media /= numeros

for i in range(len(lista)):
    lista_auxiliar.append(math.pow(lista[i] - media, 2))
    desvio_padrao += lista_auxiliar[i]

desvio_padrao = math.sqrt(desvio_padrao / 3)

print(desvio_padrao)

# 6) Faça  uma  pesquisa  sobre  os  métodos  de  lista  em  Python  apresentados  abaixo.  Em 
# seguida, apresente exemplos que demonstrem a utilização de cada um desses métodos. 
# Apresente  as  explicações  de  cada  um  deles  no  seu  notebook na  forma  de  comentários 
# Markdown juntamente com os exemplos.
# a) count ()
# b) index ()

lista = []

numeros = int(input('\nQuantos numeros vai digitar na lista? '))
for i in range(numeros):
    lista.insert(i, int(input('Digite o numero: ')))

lista_auxiliar = []

exemplo_1 = list.index(2)
exemplo_2 = list.count(4)

print('O Index retorna em qual posicão se encontra o valor informado: ', exemplo_1)
print('O count retorna quantas vezes o elemento aparece na lista')

# 7) Faça uma pesquisa sobre as funções Python apresentados abaixo. Em seguida, apresente 
# exemplos que demonstrem a utilização de cada uma delas. Apresente as explicações de 
# cada  uma  delas  no  seu  notebook  na  forma  de  texto  Markdown  juntamente  com  os 
# exemplos.
# a) min ()
# b) max ()
# c) sum ()

x = min(1, 2, 3)
print('A função min() retorna o menor número dentre os informados: ', x)

x = max(1, 2, 3)
print('A função max() retorna o maior número dentre os informados: ', x)

lista = [1, 2, 3, 4, 5]
x = sum(lista)

print('A função sum() retorna a soma de todos os valores de uma lista: ', x)