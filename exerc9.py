import numpy as np

def obter_vetor(nome):
    print(f"\n--- Vetor {nome} ---")
    while True:
        try:
            entrada = input(f"Digite as 3 componentes do vetor {nome} (ex: 1,2,3): ")
            componentes = [float(c.strip()) for c in entrada.split(',')]
            
            if len(componentes) != 3:
                print("Erro: Por favor, digite exatamente 3 componentes.")
                continue
                
            return np.array(componentes)
        except ValueError:
            print("Entrada inválida. Certifique-se de que todas as componentes são números.")

def calcular_operacoes_vetores():
    
    vetor_a = obter_vetor("A")
    vetor_b = obter_vetor("B")

    produto_escalar = np.dot(vetor_a, vetor_b)

    norma_a = np.linalg.norm(vetor_a)
    norma_b = np.linalg.norm(vetor_b)

    print("\n" + "="*50)
    print("## Resultados do Cálculo Vetorial (NumPy)")
    print("="*50)
    print(f"Vetor A: {vetor_a}")
    print(f"Vetor B: {vetor_b}")
    print("-" * 50)
    
    print(f"Produto Escalar (A · B): {produto_escalar:.2f}")
    print("\n")
    print(f"Norma do Vetor A (||A||): {norma_a:.2f}")
    print(f"Norma do Vetor B (||B||): {norma_b:.2f}")
    print("="*50 + "\n")

calcular_operacoes_vetores()