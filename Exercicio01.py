# Exercício
# 1) Ler dois números informados pelo usuário e apresentar o resultado da:
# a. Soma dos dois números.
# b. Subtração do primeiro pelo segundo número.
# c. Multitplicação dos dois números.
# d. Divisão do primeiro pelo segundo número.

primeiro = int(input("Digite o primeiro numero: "))
segundo = int(input("Digite o segundo numero: "))
print("Soma: ", (primeiro + segundo))
print("Subtracao: ", (primeiro - segundo))
print("Multiplicacao: ", (primeiro * segundo))
print("Divisao: ", (primeiro / segundo))

# 2) Ler três números informados pelo usuário e apresentar o resultado da media aritmética dos três números.

media = (int(input("\nDigite o primeiro: ")) +
         int(input("Digite o segundo: ")) + int(input("Digite o terceiro: "))) / 3
print("Media: ", media)
