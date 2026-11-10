
# ==================================================
# Aluno: Joao Pedro De Rodrigues Alves
# Matricula: 2312130223
# Disciplina: Estruturas Matematicas para Computacao
# Curso: Ciencia da Computacao
# Turno: Matutino
# Atividade 1 - Congruencia Modular

print(" VERIFICACAO DE CONGRUENCIA MODULAR ")

# Solicita os valores ao usuario
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
n = int(input("Digite o modulo n: "))

# Verifica se o modulo e positivo
while n <= 0:
    print("O modulo deve ser maior que zero!")
    n = int(input("Digite novamente o modulo n: "))

# Calcula a diferenca entre os valores
diferenca = a - b

# Calcula o resto da divisao
resto = diferenca % n

# Apresenta os calculos
print("\n========== CALCULOS ==========")
print(f"Diferenca: {a} - {b} = {diferenca}")
print(f"Resto da divisao: {diferenca} % {n} = {resto}")

# Verifica a congruencia
print("\n========== RESULTADO ==========")

if resto == 0:
    print(f"{a} e congruente a {b} modulo {n}.")
    print("A diferenca e divisivel pelo modulo.")
else:
    print(f"{a} nao e congruente a {b} modulo {n}.")
    print("A diferenca nao e divisivel pelo modulo.")

