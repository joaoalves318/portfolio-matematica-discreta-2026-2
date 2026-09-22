# ==============================================
nome = "João Pedro De Rodrigues Alves"
matricula = "2312130223"
disciplina = "Estruturas Matemáticas para Computação"
turno = "Matutino"
# ==============================================

print("==============================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("==============================================")
print("Nome:", nome)
print("Matrícula:", matricula)
print("Disciplina:", disciplina)
print("Turno:", turno)
print("==============================================")
print("ATIVIDADE 2 - DIVISIBILIDADE, MDC E MMC")
print("==============================================")


# Entrada dos números
a = int(input("Digite o primeiro número inteiro positivo: "))
b = int(input("Digite o segundo número inteiro positivo: "))


# Verifica se os números são positivos
while a <= 0 or b <= 0:
    print("Os números precisam ser positivos.")

    a = int(input("Digite o primeiro número inteiro positivo: "))
    b = int(input("Digite o segundo número inteiro positivo: "))


# Divisão inteira e resto
div = a // b
mod = a % b

print("\n----------------------------------------------")
print("DIVISÃO INTEIRA E RESTO")
print("----------------------------------------------")
print(a, "DIV", b, "=", div)
print(a, "MOD", b, "=", mod)


# Guarda os números originais
numero1 = a
numero2 = b


# Coloca o maior número primeiro para usar o Algoritmo de Euclides
if a < b:
    a, b = b, a


print("\n----------------------------------------------")
print("ALGORITMO DE EUCLIDES")
print("----------------------------------------------")


# Algoritmo de Euclides
while b != 0:
    quociente = a // b
    resto = a % b

    print(a, "=", b, "x", quociente, "+", resto)

    a = b
    b = resto


# Quando o resto chega a zero, o valor de a é o MDC
mdc = a

print("\nMDC =", mdc)


# Cálculo do MMC
mmc = (numero1 * numero2) // mdc

print("\n----------------------------------------------")
print("MMC")
print("----------------------------------------------")
print("MMC =", mmc)


print("\n==============================================")
print("Programa finalizado.")
print("==============================================")
