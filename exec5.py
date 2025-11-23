def obter_matriz_2x3():
    matriz = []
    linhas = 2
    colunas = 3
    print("##  Entrada de Dados")
    print("Preencha a matriz 2x3 (2 linhas, 3 colunas, total de 6 números).")
    print("---")
    
    for i in range(linhas):
        linha = []
        for j in range(colunas):
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

def calcular_transposta(matriz_original):
    linhas_orig = len(matriz_original)
    colunas_orig = len(matriz_original[0])
    
    matriz_transposta = []
    
    for j in range(colunas_orig):
        nova_linha = []
        for i in range(linhas_orig):
            nova_linha.append(matriz_original[i][j])
        matriz_transposta.append(nova_linha)
        
    return matriz_transposta

def exibir_matriz(m):
    if not m:
        return
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

matriz_A = obter_matriz_2x3()
matriz_T = calcular_transposta(matriz_A)

print("\n" + "="*50)
print("             Matriz e Sua Transposta             ")
print("="*50)

print("Matriz Original (2x3):")
exibir_matriz(matriz_A)
print("---")

print("Matriz Transposta (3x2):")
exibir_matriz(matriz_T)
print("="*50 + "\n")