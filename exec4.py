def gerar_matriz_identidade_4x4():
    tamanho = 4
    matriz_identidade = []

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz_identidade.append(linha)
    
    return matriz_identidade

def exibir_matriz(m):
    largura_maxima = 0
    for linha in m:
        for elemento in linha:
            comprimento = len(str(elemento))
            if comprimento > largura_maxima:
                largura_maxima = comprimento
    largura_maxima += 2
    for linha in m:
        linha_str = ""
        for elemento in linha:
            linha_str += f"{elemento:>{largura_maxima}}" 
        print(f"|{linha_str} |")

matriz_I4 = gerar_matriz_identidade_4x4()

print("##  Matriz Identidade 4x4")
print("A matriz identidade é gerada onde M[i][j] = 1 se i=j e 0 se i≠j.")
print("="*30)
exibir_matriz(matriz_I4)
print("="*30)