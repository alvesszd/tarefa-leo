def calcular_diagonal_principal_e_soma(matriz_3x3):
    diagonal = []
    soma_diagonal = 0
    tamanho = 3

    for i in range(tamanho):
        elemento = matriz_3x3[i][i]
        diagonal.append(elemento)
        soma_diagonal += elemento
        
    return diagonal, soma_diagonal

def obter_matriz_do_usuario():
    matriz = []
    tamanho = 3
    print("##  Entrada de Dados")
    print("Preencha a matriz 3x3 (9 números) para calcular a diagonal principal.")
    print("---")
    
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            while True:
                try:
                    valor = input(f"Digite o número para a posição ({i+1},{j+1}): ")
                    numero = float(valor)
                    linha.append(numero)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)
    return matriz

def exibir_matriz(m):
    largura_maxima = 0
    for linha in m:
        for elemento in linha:
            comprimento = len(f"{elemento:.2f}")
            if comprimento > largura_maxima:
                largura_maxima = comprimento
    largura_maxima += 2
    for linha in m:
        linha_str = ""
        for elemento in linha:
            linha_str += f"{elemento:>{largura_maxima}.2f}" 
        print(f"|{linha_str} |")

matriz_usuario = obter_matriz_do_usuario()

print("\n" + "="*50)
print("          Cálculo da Diagonal Principal          ")
print("="*50)

print("Matriz Digitada:")
exibir_matriz(matriz_usuario)
print("---")

diagonal_principal, soma = calcular_diagonal_principal_e_soma(matriz_usuario)

print(f" Elementos da Diagonal Principal: **{diagonal_principal}**")
print(f" A Soma desses valores é: **{soma:.2f}**")
print("="*50 + "\n")