import pandas as pd
import numpy as np
import os

# --- 1. Criação do Arquivo CSV de Exemplo ---
nome_arquivo = 'dados_exemplo.csv'

data = {
    'x': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
    'y': [7.1, 9.2, 11.0, 12.9, 15.1, 17.0]
}
df_exemplo = pd.DataFrame(data)
df_exemplo.to_csv(nome_arquivo, index=False)

print(f"Arquivo de exemplo '{nome_arquivo}' criado com sucesso.")
print("--------------------------------------")

# --- 2. Leitura e Preparação dos Dados ---
try:
    df = pd.read_csv(nome_arquivo)
    
    x = df['x'].values
    y = df['y'].values
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
    exit()

# --- 3. Cálculo da Regressão Linear (Mínimos Quadrados) ---
coeficientes = np.polyfit(x, y, 1)

a = coeficientes[0]
b = coeficientes[1]

# --- 4. Exibição dos Resultados ---
print("## Resultados da Regressão Linear")
print(f"Dados lidos do arquivo '{nome_arquivo}':")
print(df.head())
print("--------------------------------------")

print(f"A equação da reta ajustada (y = a*x + b) é:")
print(f"y = {a:.4f} * x + {b:.4f}")

print("\n")
print(f"a (Inclinação/Slope): {a:.4f}")
print(f"b (Intercepto): {b:.4f}")
print("--------------------------------------")

os.remove(nome_arquivo)