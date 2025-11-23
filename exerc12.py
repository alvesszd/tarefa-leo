import os

arquivo_numeros = 'numeros.txt'
arquivo_resumo = 'resumo.txt'

# --- 1. Criação e Escrita no Arquivo de Entrada ---
conteudo_numeros = "10\n25.5\n5\n12.5\n47"

try:
    with open(arquivo_numeros, 'w') as f:
        f.write(conteudo_numeros)
    print(f"Arquivo de números '{arquivo_numeros}' criado com sucesso.")
    print("--------------------------------------")
except IOError as e:
    print(f"Erro ao criar o arquivo de números: {e}")
    exit()

# --- 2. Leitura, Cálculo e Processamento ---
numeros = []
soma = 0
media = 0

try:
    with open(arquivo_numeros, 'r') as f:
        for linha in f:
            try:
                numero = float(linha.strip())
                numeros.append(numero)
                soma += numero
            except ValueError:
                print(f"Aviso: Linha inválida ignorada: {linha.strip()}")

    if numeros:
        media = soma / len(numeros)

    print(f"Números lidos: {numeros}")
    print(f"Soma calculada: {soma:.2f}")
    print(f"Média calculada: {media:.2f}")
    print("--------------------------------------")

# --- 3. Escrita dos Resultados no Arquivo de Resumo ---
    conteudo_resumo = (
        f"Soma Total: {soma:.2f}\n"
        f"Média Aritmética: {media:.2f}\n"
        f"Total de Números Lidos: {len(numeros)}"
    )

    with open(arquivo_resumo, 'w') as f:
        f.write(conteudo_resumo)
    
    print(f"Resultados salvos em '{arquivo_resumo}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_numeros}' não foi encontrado.")
except IOError as e:
    print(f"Erro ao ler ou escrever arquivos: {e}")

# --- 4. Limpeza (Opcional) ---
if os.path.exists(arquivo_numeros):
    os.remove(arquivo_numeros)
if os.path.exists(arquivo_resumo):
    os.remove(arquivo_resumo)