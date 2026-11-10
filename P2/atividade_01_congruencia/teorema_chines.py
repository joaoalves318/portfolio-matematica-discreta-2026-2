
# ==================================================
# Aluno: Joao Pedro De Rodrigues Alves
# Matricula: 2312130223
# Disciplina: Estruturas Matematicas para Computacao
# Curso: Ciencia da Computacao
# Turno: Matutino
# Atividade 1 - Parte B: Teorema Chines do Resto


# Calcula o MDC utilizando o Algoritmo de Euclides
def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


# Calcula o inverso multiplicativo usando Euclides Estendido
def calcular_inverso(a, modulo):
    m = modulo
    x0 = 0
    x1 = 1

    while a > 1:
        quociente = a // modulo

        auxiliar = modulo
        modulo = a % modulo
        a = auxiliar

        auxiliar = x0
        x0 = x1 - quociente * x0
        x1 = auxiliar

    return x1 % m


print("=== TEOREMA CHINES DO RESTO ===")

# Escolha da quantidade de congruencias
quantidade = int(input("Digite a quantidade de congruencias (3 ou 4): "))

while quantidade != 3 and quantidade != 4:
    print("A quantidade deve ser 3 ou 4!")
    quantidade = int(input("Digite novamente: "))

# Listas para guardar os restos e os modulos
restos = []
modulos = []

# Recebe os valores de cada congruencia
for i in range(quantidade):
    print(f"\nCongruencia {i + 1}")

    a = int(input("Digite o resto: "))
    n = int(input("Digite o modulo: "))

    while n <= 0:
        print("O modulo deve ser positivo!")
        n = int(input("Digite novamente o modulo: "))

    restos.append(a)
    modulos.append(n)


# Verifica se os modulos sao dois a dois coprimos
coprimos = True

for i in range(quantidade):
    for j in range(i + 1, quantidade):
        mdc = calcular_mdc(modulos[i], modulos[j])

        print(f"MDC({modulos[i]}, {modulos[j]}) = {mdc}")

        if mdc != 1:
            coprimos = False

if not coprimos:
    print("\nOs modulos nao sao dois a dois coprimos.")
    print("O sistema esta fora das condicoes da atividade.")

else:
    # Calcula o produto de todos os modulos
    N = 1

    for n in modulos:
        N = N * n

    print("\n=== CALCULO DO PRODUTO ===")
    print(f"Produto dos modulos: N = {N}")

    resultado = 0

    # Calcula Ni e o inverso multiplicativo
    for i in range(quantidade):
        Ni = N // modulos[i]

        inverso = calcular_inverso(Ni, modulos[i])

        parcela = restos[i] * Ni * inverso

        resultado = resultado + parcela

        print(f"\nCongruencia {i + 1}:")
        print(f"Resto: {restos[i]}")
        print(f"Modulo: {modulos[i]}")
        print(f"N{i + 1} = {N} / {modulos[i]} = {Ni}")
        print(f"Inverso de {Ni} modulo {modulos[i]} = {inverso}")
        print(f"Parcela: {restos[i]} * {Ni} * {inverso} = {parcela}")

    # Reduz o resultado ao modulo N
    x0 = resultado % N

    print("\n=== RESULTADO FINAL ===")
    print(f"Solucao particular: x0 = {x0}")
    print(f"Modulo total: N = {N}")
    print(f"Solucao geral: x = {x0} + {N} * t, com t pertencente aos inteiros")

    # Verifica se a solucao satisfaz todas as congruencias
    print("\n=== VERIFICACAO DAS CONGRUENCIAS ===")

    for i in range(quantidade):
        resto_calculado = x0 % modulos[i]

        print(f"{x0} % {modulos[i]} = {resto_calculado}")

        if resto_calculado == restos[i] % modulos[i]:
            print("Congruencia satisfeita!")
        else:
            print("Erro na verificacao!")
