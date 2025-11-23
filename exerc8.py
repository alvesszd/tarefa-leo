import numpy as np

A = np.array([
    [2, 1],
    [1, -1]
])

b = np.array([5, 1])

solucao = np.linalg.solve(A, b)

print("##  Solução do Sistema Linear")
print("--------------------------------------")
print("Matriz de Coeficientes (A):")
print(A)
print("\nVetor de Resultados (b):")
print(b)
print("\n--------------------------------------")
print(f"O Vetor Solução [x, y] é: **{solucao}**")

x = solucao[0]
y = solucao[1]

print(f"\nPortanto, a solução é **x = {x:.2f}** e **y = {y:.2f}**.")
print("--------------------------------------")