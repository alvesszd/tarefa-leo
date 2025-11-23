import os

nome_arquivo = 'dados.txt'

conteudo_exemplo = (
    "Esta é a primeira linha do arquivo.\n"
    "A segunda linha tem algumas palavras, incluindo: Python e Código.\n"
    "Terceira linha, final."
)

with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write(conteudo_exemplo)

print(f"Arquivo de exemplo '{nome_arquivo}' criado com sucesso.")
print("Conteúdo:")
print(conteudo_exemplo)
print("--------------------------------------")


def contar_linhas_e_palavras(caminho_arquivo):
    
    total_linhas = 0
    total_palavras = 0
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                total_linhas += 1
                palavras = linha.strip().split()
                total_palavras += len(palavras)
                
        return total_linhas, total_palavras
        
    except FileNotFoundError:
        return 0, 0


linhas, palavras = contar_linhas_e_palavras(nome_arquivo)

print("## Resultados da Análise do Arquivo")
print("--------------------------------------")
print(f"Total de Linhas no arquivo: {linhas}")
print(f"Total de Palavras no arquivo: {palavras}")
print("--------------------------------------")

if os.path.exists(nome_arquivo):
    os.remove(nome_arquivo)