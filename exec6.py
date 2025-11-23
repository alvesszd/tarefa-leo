import numpy as np

np.random.seed(42)


matriz_a = np.random.randint(low=1, high=11, size=(2, 2))
matriz_b = np.random.randint(low=1, high=11, size=(2, 2))

print("##  Matrizes Originais")
print("---")
print("Matriz A:")
print(matriz_a)
print("\nMatriz B:")
print(matriz_b)


soma_matrizes = matriz_a + matriz_b
print("\n" + "="*30)
print(" Soma das Matrizes (A + B):")
print(soma_matrizes)

multiplicacao_matricial = matriz_a @ matriz_b
print("\n" + "="*30)
print(" Multiplicação Matricial (A @ B):")
print(multiplicacao_matricial)

# C. Transpostas
transposta_a = matriz_a.T
transposta_b = matriz_b.T
print("\n" + "="*30)
print("ᵀ Transposta da Matriz A:")
print(transposta_a)

print("\n" + "="*30)
print("ᵀ Transposta da Matriz B:")
print(transposta_b)
print("="*30)