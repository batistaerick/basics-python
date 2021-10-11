# 1) Escreva um algoritmo em linguagem de programação Python que leia um número a partir
# do teclado e que informe se o número é par ou ímpar.

numero = int(input('Digite o numero: '))

if numero % 2 == 0:
    print('Numero PAR')
else:
    print('Numero Impar')


# 2) Escreva  um  algoritmo  em  linguagem  de  programação  Python  que  leia  a  coordenada
# cartesiana de um ponto. O algoritmo deve imprimir a coordenada do ponto e o quadrante
# em que o ponto está situado. Se o ponto estiver na origem, imprimir: "Ponto situado na
# origem  do  plano  cartesiano.".  Por  outro  lado,  se  o  ponto  estiver  situado sobre um dos
# eixos, informar se o ponto situa-se na parte positiva ou negativa do eixo X ou Y.

x = int(input('\nInforme a abscissa do ponto:'))
y = int(input('Informe a ordenada do ponto:'))

if x > 0 and y > 0:
    print("Quadrante 1")

elif x < 0 and y > 0:
    print("Quadrante 2")

elif x < 0 and y < 0:
    print("Quadrante 3")

elif x > 0 and y < 0:
    print("Quadrante 4")

elif x == 0 and y == 0:
    print("Ponto situado na origem do plano cartesiano.")

elif x > 0 and y == 0:
    print("Parte Positiva")

elif x < 0 and y == 0:
    print('Parte Negativa')

elif x == 0 and y > 0:
    print("Parte Positiva")

elif x == 0 and y < 0:
    print("Parte Negativa")
