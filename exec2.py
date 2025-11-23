def calcular_soma_matriz_3x3():
    """
    Cria uma matriz 3x3 com números fornecidos pelo usuário, 
    exibe a matriz e calcula a soma de todos os seus elementos.
    """
    matriz = []
    tamanho = 3
    soma_total = 0
    
    print("## 🔢 Entrada de Dados")
    print("Preencha a matriz 3x3 (9 números).")
    print("---")

    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            while True:
                try:
                    valor = input(f"Digite o número para a posição ({i+1},{j+1}): ")
                    numero = float(valor)
                    linha.append(numero)
                    
                    soma_total += numero
                    
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        matriz.append(linha)
    
    print("\n" + "="*35)
    print("     Matriz 3x3 e Resultado      ")
    print("="*35)

    largura_maxima = 0
    for linha in matriz:
        for elemento in linha:
            comprimento = len(f"{elemento:.2f}")
            if comprimento > largura_maxima:
                largura_maxima = comprimento

    largura_maxima += 2

    print("Matriz Digitada:")
    for linha in matriz:
        linha_str = ""
        for elemento in linha:
            linha_str += f"{elemento:>{largura_maxima}.2f}" 
            
        print(f"|{linha_str} |")
        
    print("---")
    
    print(f" A **SOMA de todos os elementos** é: **{soma_total:.2f}**")
    print("="*35 + "\n")


calcular_soma_matriz_3x3()
