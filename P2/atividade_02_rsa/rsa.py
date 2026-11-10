
# ATIVIDADE 2 - CRIPTOGRAFIA RSA
# Parte A - Primalidade e parametros RSA

# Verifica se um numero e primo
def verificar_primo(numero):
    if numero < 2:
        return False

    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


# Solicita dois numeros primos diferentes
print("\n===== PARTE A - PARAMETROS RSA =====")

p = int(input("Digite o primeiro numero primo (p): "))
q = int(input("Digite o segundo numero primo (q): "))

# Verifica se os numeros sao maiores que 1 e diferentes
while p <= 1 or q <= 1 or p == q:
    print("Os numeros devem ser maiores que 1 e diferentes.")
    p = int(input("Digite novamente p: "))
    q = int(input("Digite novamente q: "))

# Verifica se os dois numeros sao primos
while not verificar_primo(p) or not verificar_primo(q):
    print("Os dois numeros devem ser primos.")
    p = int(input("Digite novamente p: "))
    q = int(input("Digite novamente q: "))

# Calcula o modulo RSA
n = p * q

# Calcula a funcao totiente de Euler
phi = (p - 1) * (q - 1)

# Apresenta os resultados
print("\n===== RESULTADOS DA PARTE A =====")
print(f"Numero primo p: {p}")
print(f"Numero primo q: {q}")
print(f"Modulo RSA: n = {p} x {q} = {n}")
print(f"Funcao totiente: phi(n) = {phi}")

# Solicita o expoente publico
e = int(input("\nDigite o expoente publico e: "))

# Verifica se o expoente atende as condicoes
while e <= 1 or e >= phi:
    print("O expoente deve ser maior que 1 e menor que phi(n).")
    e = int(input("Digite novamente o expoente e: "))

# Verifica se o MDC entre e e phi(n) e igual a 1
def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


while calcular_mdc(e, phi) != 1:
    print("O expoente e nao e coprimo com phi(n).")
    e = int(input("Digite outro expoente publico e: "))

print(f"\nExpoente publico escolhido: e = {e}")
print("\nParte A concluida!")


# PARTE B - CONSTRUCAO DAS CHAVES RSA


# Calcula o inverso multiplicativo pelo algoritmo
# de Euclides Estendido
def calcular_inverso(e, phi):
    a = e
    b = phi

    x0 = 1
    x1 = 0

    while b != 0:
        quociente = a // b
        resto = a % b

        a = b
        b = resto

        auxiliar = x0 - quociente * x1
        x0 = x1
        x1 = auxiliar

    return x0 % phi


# Calcula o expoente privado
d = calcular_inverso(e, phi)

# Verifica se o inverso esta correto
verificacao = (e * d) % phi

print("\n===== PARTE B - CONSTRUCAO DAS CHAVES =====")
print(f"Calculo do inverso: d = {d}")
print(f"Verificacao: {e} x {d} mod {phi} = {verificacao}")

if verificacao == 1:
    print("\nChaves RSA construidas com sucesso!")
    print(f"Chave publica: (e, n) = ({e}, {n})")
    print(f"Chave privada: (d, n) = ({d}, {n})")
else:
    print("Erro na construcao das chaves.")


# PARTE C - CIFRAGEM E DECIFRAGEM


# Solicita uma mensagem numerica
print("\n===== PARTE C - CIFRAGEM E DECIFRAGEM =====")

mensagem = int(input("Digite um numero para criptografar: "))

# Verifica se a mensagem esta dentro do intervalo permitido
while mensagem < 0 or mensagem >= n:
    print(f"O numero deve estar entre 0 e {n - 1}.")
    mensagem = int(input("Digite novamente a mensagem: "))

# Realiza a exponenciacao modular
def potencia_modular(base, expoente, modulo):
    resultado = 1
    base = base % modulo

    while expoente > 0:
        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo

        base = (base * base) % modulo
        expoente = expoente // 2

    return resultado


# Criptografa a mensagem usando a chave publica
cifrado = potencia_modular(mensagem, e, n)

# Descriptografa usando a chave privada
decifrado = potencia_modular(cifrado, d, n)

# Apresenta os resultados
print("\n===== RESULTADO DA CRIPTOGRAFIA =====")
print(f"Mensagem original: {mensagem}")
print(f"Calculo da cifragem: {mensagem}^{e} mod {n} = {cifrado}")
print(f"Numero criptografado: {cifrado}")
print(f"Calculo da decifragem: {cifrado}^{d} mod {n} = {decifrado}")
print(f"Mensagem recuperada: {decifrado}")

if mensagem == decifrado:
    print("\nCriptografia e decifragem realizadas com sucesso!")
else:
    print("\nErro na recuperacao da mensagem.")


# PARTE D - TEOREMAS DE FERMAT E EULER


print("\n===== PARTE D - TEOREMAS DE FERMAT E EULER =====")

# Solicita os valores para demonstracao
base = int(input("Digite uma base positiva: "))
modulo = int(input("Digite um modulo maior que 1: "))

while base <= 0 or modulo <= 1:
    print("A base deve ser positiva e o modulo maior que 1.")
    base = int(input("Digite novamente a base: "))
    modulo = int(input("Digite novamente o modulo: "))

# Verifica se a base e o modulo sao coprimos
mdc = calcular_mdc(base, modulo)

print(f"\nMDC({base}, {modulo}) = {mdc}")

# Calcula a funcao totiente do modulo informado
phi_modulo = 0

for i in range(1, modulo + 1):
    if calcular_mdc(i, modulo) == 1:
        phi_modulo += 1

# Aplica o Teorema de Euler
print("\n===== TEOREMA DE EULER =====")

if mdc == 1:
    resultado_euler = potencia_modular(base, phi_modulo, modulo)

    print(f"Funcao totiente de {modulo}: {phi_modulo}")
    print(f"{base}^{phi_modulo} mod {modulo} = {resultado_euler}")

    if resultado_euler == 1:
        print("Teorema de Euler verificado!")
else:
    print("A base e o modulo nao sao coprimos.")
    print("Nao e possivel aplicar o Teorema de Euler.")

# Aplica o Pequeno Teorema de Fermat
print("\n===== PEQUENO TEOREMA DE FERMAT =====")

p_fermat = int(input("Digite um modulo primo: "))
a_fermat = int(input("Digite uma base positiva: "))

while not verificar_primo(p_fermat) or a_fermat <= 0:
    print("Informe um modulo primo e uma base positiva.")
    p_fermat = int(input("Digite novamente o modulo primo: "))
    a_fermat = int(input("Digite novamente a base: "))

if a_fermat % p_fermat != 0:
    resultado_fermat = potencia_modular(
        a_fermat, p_fermat - 1, p_fermat
    )

    print(f"\n{a_fermat}^{p_fermat - 1} mod {p_fermat} = {resultado_fermat}")

    if resultado_fermat == 1:
        print("Pequeno Teorema de Fermat verificado!")
else:
    print("A base e divisivel pelo modulo.")
    print("Nao e possivel aplicar o teorema.")

print("\n===== ATIVIDADE 2 CONCLUIDA =====")
