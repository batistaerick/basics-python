# 1) Escreva  um  algoritmo  que  solicite  como  entrada  um  limite  inferior natural e um limite
# superior também natural. O algoritmo deve apresentar na tela todos os números pares
# entre o limite inferior e superior. Os limites inferior e superior devem ser apresentados
# se também forem números pares.

limite_inferior = int(input('\nDigite o limite inferior natural: '))
limite_superior = int(input('\nDigite o limite superior natural: '))

pares = 0

if limite_superior < limite_inferior or limite_superior <= 0 or limite_inferior < 0:
    print('\nLimites informados nao sao validos.')
else:
    while limite_inferior <= limite_superior:

        if limite_inferior % 2 == 0:
            pares += 1
            print(limite_inferior)
        limite_inferior += 1

print('Existem {} número(s) par(es).'.format(pares))

# Escreva  um  algoritmo  que  leia  um  número  natural  informado  pelo  usuário  a  partir  do
# teclado  e  que  apresente  como  saída  o  fatorial  desse  número.  Se  o  usuário  inserir  um
# número negativo, o algoritmo deve informar que o número é inválido.

fatorial = int(input('Digite um numero: '))

if (fatorial < 0):
    print('Valor informado e menor que zero')
else:
    x = fatorial - 1

    while x > 0:
        fatorial *= x
        x -= 1

print('O valor fatorial e {} .'.format(fatorial))
