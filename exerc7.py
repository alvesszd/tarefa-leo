import numpy as np

np.random.seed(42)

def calcular_determinante_3x3():
    matriz = np.random.randint(1, 11, size=(3, 3))
    
    determinante = np.linalg.det(matriz)
    
    print("## Cálculo do Determinante")
    print("--------------------------------------")
    
    print("Matriz A (Gerada Aleatoriamente):")
    print(matriz)
    
    print("\n--------------------------------------")
    print(f"O Determinante de A é: {determinante:.2f}")
    print("--------------------------------------")

calcular_determinante_3x3()
