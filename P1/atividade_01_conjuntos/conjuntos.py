```python
nome = "João Pedro De Rodrigues Alves"
matricula = "2312130223"
disciplina = "Estruturas Matemáticas para Computação"
turno = "Matutino"


# Mostra um conjunto no formato {1, 2, 3}
def mostrar_conjunto(conjunto):
    return "{" + ", ".join(str(x) for x in conjunto) + "}"


# Calcula a união de A e B
def uniao(A, B):
    resultado = A.copy()

    for elemento in B:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado


# Calcula a interseção de A e B
def intersecao(A, B):
    resultado = []

    for elemento in A:
        if elemento in B:
            resultado.append(elemento)

    return resultado


# Calcula A - B
def diferenca(A, B):
    resultado = []

    for elemento in A:
        if elemento not in B:
            resultado.append(elemento)

    return resultado


# Verifica se A está contido em B
def esta_contido(A, B):
    for elemento in A:
        if elemento not in B:
            return False

    return True


# Calcula o conjunto das partes
def conjunto_das_partes(A):
    partes = [[]]

    for elemento in A:
        novas_partes = []

        for parte in partes:
            nova = parte.copy()
            nova.append(elemento)
            novas_partes.append(nova)

        partes = partes + novas_partes

    return partes


# Mostra o conjunto das partes
def mostrar_partes(partes):
    resultado = []

    for parte in partes:
        resultado.append(mostrar_conjunto(parte))

    return "{" + ", ".join(resultado) + "}"


# Calcula o produto cartesiano A x B
def produto_cartesiano(A, B):
    resultado = []

    for a in A:
        for b in B:
            resultado.append((a, b))

    return resultado


# ==============================================
# CABEÇALHO
# ==============================================

print("==============================================")
print("PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA")
print("==============================================")
print("Nome:", nome)
print("Matrícula:", matricula)
print("Disciplina:", disciplina)
print("Turno:", turno)
print("==============================================")
print("ATIVIDADE 1 - TEORIA DOS CONJUNTOS")
print("==============================================")


# ==============================================
# ENTRADA DOS CONJUNTOS
# ==============================================

entrada_A = input("Digite os elementos de A separados por espaço: ")
entrada_B = input("Digite os elementos de B separados por espaço: ")

A = []
B = []

for valor in entrada_A.split():
    numero = int(valor)

    if numero not in A:
        A.append(numero)

for valor in entrada_B.split():
    numero = int(valor)

    if numero not in B:
        B.append(numero)


# ==============================================
# OPERAÇÕES COM OS CONJUNTOS
# ==============================================

uniao_AB = uniao(A, B)
intersecao_AB = intersecao(A, B)
diferenca_AB = diferenca(A, B)
diferenca_BA = diferenca(B, A)


# ==============================================
# CONJUNTO DAS PARTES
# ==============================================

partes_A = conjunto_das_partes(A)
partes_B = conjunto_das_partes(B)


# ==============================================
# PRODUTO CARTESIANO
# ==============================================

cartesiano = produto_cartesiano(A, B)


# ==============================================
# RESULTADOS
# ==============================================

print("\n----------------------------------------------")
print("CONJUNTOS")
print("----------------------------------------------")
print("A =", mostrar_conjunto(A))
print("B =", mostrar_conjunto(B))


print("\n----------------------------------------------")
print("1. UNIÃO")
print("----------------------------------------------")
print("A ∪ B =", mostrar_conjunto(uniao_AB))


print("\n----------------------------------------------")
print("2. INTERSEÇÃO")
print("----------------------------------------------")
print("A ∩ B =", mostrar_conjunto(intersecao_AB))


print("\n----------------------------------------------")
print("3. DIFERENÇAS")
print("----------------------------------------------")
print("A - B =", mostrar_conjunto(diferenca_AB))
print("B - A =", mostrar_conjunto(diferenca_BA))


print("\n----------------------------------------------")
print("4. CARDINALIDADES")
print("----------------------------------------------")
print("|A| =", len(A))
print("|B| =", len(B))
print("|A ∪ B| =", len(uniao_AB))
print("|A ∩ B| =", len(intersecao_AB))


print("\n----------------------------------------------")
print("5. CONJUNTO DAS PARTES")
print("----------------------------------------------")
print("P(A) =", mostrar_partes(partes_A))
print("P(B) =", mostrar_partes(partes_B))


print("\n----------------------------------------------")
print("6. CARDINALIDADE DOS CONJUNTOS DAS PARTES")
print("----------------------------------------------")
print("|P(A)| =", len(partes_A))
print("|P(B)| =", len(partes_B))


print("\n----------------------------------------------")
print("7. EXEMPLO DE PARTIÇÃO")
print("----------------------------------------------")

if len(A) == 0:
    print("A está vazio, então não será mostrada uma partição.")
elif len(A) == 1:
    print("Uma partição de A é:", mostrar_conjunto(A))
else:
    meio = len(A) // 2

    grupo1 = A[:meio]
    grupo2 = A[meio:]

    print("A =", mostrar_conjunto(A))
    print("Partição de A:")
    print(mostrar_conjunto(grupo1), "e", mostrar_conjunto(grupo2))


print("\n----------------------------------------------")
print("8. PRODUTO CARTESIANO")
print("----------------------------------------------")

if len(cartesiano) == 0:
    print("A x B = {}")
else:
    pares = []

    for par in cartesiano:
        pares.append("(" + str(par[0]) + ", " + str(par[1]) + ")")

    print("A x B =", "{" + ", ".join(pares) + "}")


print("\n----------------------------------------------")
print("9. INCLUSÃO")
print("----------------------------------------------")

if esta_contido(A, B):
    print("A está contido em B: A ⊆ B")
else:
    print("A não está contido em B: A ⊄ B")

if esta_contido(B, A):
    print("B está contido em A: B ⊆ A")
else:
    print("B não está contido em A: B ⊄ A")


print("\n==============================================")
print("Programa finalizado.")
print("==============================================")
```
