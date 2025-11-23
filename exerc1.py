def criar_e_exibir_matriz_3x3():
    matriz = []
    tamanho = 3
    
    print("Preencha a matriz 3x3. Você precisará fornecer 9 números no total.")
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
    
    print("\n" + "="*30)
    print("       Matriz 3x3 Preenchida       ")
    print("="*30)

    largura_maxima = 0
    for linha in matriz:
        for elemento in linha:
            comprimento = len(f"{elemento:.2f}")
            if comprimento > largura_maxima:
                largura_maxima = comprimento

    largura_maxima += 2

    for linha in matriz:
        linha_str = ""
        for elemento in linha:
            linha_str += f"{elemento:>{largura_maxima}.2f}" 
            
        print(f"|{linha_str} |")
        
    print("="*30 + "\n")


criar_e_exibir_matriz_3x3()