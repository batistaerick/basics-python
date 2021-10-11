# 1) Em um estacionamento há carros e motos. Escreva um algoritmo em linguagem de
# programação Python que solicite ao usuário o total de veículos e o total de rodas. O
# algoritmo deve determinar quantos carros e quantas motos há no estacionamento. O
# resultado deve ser apresentado para o usuário. Acrescente comentários Python em seu algoritmo.

veiculos = int(input("Digite o total de veiculos: "))
rodas = int(input("Digite o total de rodas: "))
motos = (4 * veiculos - rodas) / 2
carros = veiculos - motos
print("total de carros: %d, total de motos: %d" % (carros, motos))


# 2) Em linguagem de programação Python, escreva o algoritmo de uma máquina de venda
# automática de salgadinhos, doces, sucos e refrigerantes. O algoritmo deve calcular o
# menor número de notas que deve ser dado de troco para um pagamento efetuado. O
# algoritmo deve ler o valor da compra e o valor pago. Se o valor pago for menor que o
# valor da compra, a máquina deve apresentar uma mensagem informando que o valor
# pago é insuficiente para realizar a compra. A máquina aceita apenas notas de R$ 50,00,
# R$ 20,00, R$ 10,00, R$ 5,00, R$ 2,00 e R$ 1,00. Acrescente comentários Python em seualgoritmo.

valor_compra = int(input("\nDigite o valor do produto: "))
valor_pago = int(input("Digite o valor pago: "))

if valor_pago < valor_compra:
    print('O valor pago é insuficiente para realizar a compra!')
else:
    troco = valor_pago - valor_compra

    # Quantidade de notas de 50
    qnt_cinquenta = troco // 50
    troco = troco % 50

    # Quantidade de notas de 20
    qnt_vinte = troco // 20
    troco = troco % 20

    # Quantidade de notas de 10
    qnt_dez = troco // 10
    troco = troco % 10

    # Quantidade de notas de 5
    qnt_cinco = troco // 5
    troco = troco % 5

    # Quantidade de notas de 2
    qnt_dois = troco // 2
    troco = troco % 2

    # Quantidade de notas de 1
    qnt_um = troco // 1
    troco = troco % 1

    print('Voce tem %d notas de troco, sendo %d de R$ 50,00, %d de R$ 20,00, %d de R$ 10,00, %d de R$ 5,00, %d de R$ 2,00, %d de R$ 1,00.' % (
        (qnt_cinquenta+qnt_vinte+qnt_dez+qnt_cinco+qnt_dois+qnt_um), qnt_cinquenta, qnt_vinte, qnt_dez, qnt_cinco, qnt_dois, qnt_um))
