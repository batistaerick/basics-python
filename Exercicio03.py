# 1) Escreva um algoritmo em linguagem de programação Python que lê as coordenadas de
# dois pontos no plano cartesiano e imprima a distância entre estes dois pontos.
# OBS.: fórmula da distância entre dois pontos A (x1, y1) e B (x2, y2):

import math

x1 = int(input('Informe a abscissa do primeiro ponto (x1):'))
y1 = int(input('Informe a ordenada do primeiro ponto (y1):'))

x2 = int(input('Informe a abscissa do segundo ponto (x2):'))
y2 = int(input('Informe a ordenada do segundo ponto (y2):'))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print(f'\nA distância entre os dois pontos é {distancia}\n')

# 2) Escreva um algoritmo em linguagem de programação Python que recebe 3 valores reais
# informados pelo usuário. O algoritmo deve indicar o maior deles, o menor deles e a média
# aritmética desses números.

n1 = float(input('\nInforme o primeiro número:'))
n2 = float(input('Informe o segundo número:'))
n3 = float(input('Informe o terceiro número:'))

if n1 > n2 and n1 > n3:
    maior = n1
    print(f'\nO maior número digitado foi: {maior}\n')
elif n2 > n1 and n2 > n3:
    maior = n2
    print(f'\nO maior número digitado foi: {maior}\n')
elif n3 > n1 and n3 > n2:
    maior = n3
    3
    print(f'\nO maior número digitado foi: {maior}\n')
else:
    print(f'\n1 ou mais números digitados são iguais.')

if n1 < n2 and n1 < n3:
    menor = n1
    print(f'\nO menor número digitado foi: {menor}\n')
elif n2 < n1 and n2 < n3:
    menor = n2
    print(f'\nO menor número digitado foi: {menor}\n')
elif n3 < n1 and n3 < n2:
    menor = n3
    print(f'\nO menor número digitado foi: {menor}\n')

media = (n1+n2+n3)/3
print(f'\nO média aritmética dos 3 números é: {media}\n')

# 3) Escreva um algoritmo em linguagem de Programação Python que resolva uma equação
# de  segundo  grau,  realizando  a  verificação  de  consistência  dos  valores  dos  coeficientes
# ("a", "b" e "c") e do discriminante (delta).  a. Se os coeficientes "a" e "b" forem iguais a zero
# e o coeficiente "c" for diferente de # zero, apresentar a mensagem "Coeficientes informados
# incorretamente.". b. Caso o coeficiente "a" seja igual a zero e o coeficiente "b" for diferente de zero,
# deverá  ser  impressa  a  mensagem:  "Essa  é  uma  equação  de  primeiro  grau"  e
# deverá ser informado o valor da raiz real da equação.  c. Caso  o  discriminante  seja  negativo,
# deverá  ser  impressa  a  mensagem:  "Esta equação não possui raízes reais".  d. Caso  o
# discriminante  seja  zero,  apresentar  a  mensagem  "Esta  equação  possui
# duas raízes reais iguais. " e informar o valor das raízes da equação.  e. Caso o discriminante
# seja maior que zero, apresentar a mensagem "Esta equação possui duas raízes reais diferentes.
# " e informar o valor das raízes da equação.  Equação do segundo grau: ax2 + bx + c = 0 Discriminante:  = b2 – 4ac


a = float(input('\ninforme o A: '))
b = float(input('informe o B: '))
c = float(input('informe o C: '))
delta = (b * b) - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

if delta < 0 or math.isnan(x1) or math.isinf(x1) or math.isnan(x2) or math.isinf(x2):
    print('Impossivel calcular')
else:
    print(f'\nR1 = {x1}')
    print(f'R2 = {x2}')
