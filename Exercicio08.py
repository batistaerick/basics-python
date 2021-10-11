# 1) Escreva um algoritmo que leia uma matriz quadrada informada pelo usuário a partir do
# teclado. Uma matriz quadrada possui o número de linhas igual ao número de colunas. O
# algoritmo deve:
# A) Apresentar a diagonal principal da matriz.
# b) Apresentar a diagonal secundária da matriz.

n = int(input("Informe o tamanho da matriz: "))
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input("matriz[%d][%d] = " % (i, j))))
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        if(i == j):
            print(matriz[i][j])

for i in range(n):
    for j in range(n):
        if ((i + j) == (n - 1)):
            print(matriz[i][j])

# 2) Escreva um algoritmo que leia os elementos de duas matrizes 5x5 a partir do teclado e
# que calcule a soma das duas matrizes. Apresente a matriz resultante na tela. Exemplo: Soma:

n = 5
matriz = []
matriz_aux = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input("matriz[%d][%d] = " % (i, j))))
    matriz.append(linha)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input("matriz[%d][%d] = " % (i, j))))
    matriz_aux.append(linha)

for i in range(n):
    for j in range(n):
        matriz[i][j] = matriz_aux[i][j] + matriz[i][j]

print(matriz)


# 3. Escreva um algoritmo que leia os elementos de duas matrizes 4x4 a partir do teclado e 
# apresente o resultado da multiplicação da primeira matriz pela segunda.

