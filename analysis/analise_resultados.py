import pandas as pd

# Definir faixas para ranqueamento
faixas = {
    "5 ou inferior": (-float("inf"), 5),
    "6 a 10": (6, 10),
    "10 a 15": (10, 15),
    "acima de 15": (15, float("inf"))
}

def classificar_pontuacao(valor):
    """
    Classifica a pontuação em Grave, Alto, Médio, Baixo ou Excelente.
    """
    for nivel, (inicio, fim) in faixas.items():
        if inicio <= valor < fim:
            return nivel
    return "Não classificado"

def processar_fatores_para_ranqueamento(arquivo_entrada, arquivo_saida):
    """
    Processa o arquivo gerado anteriormente, extrai os fatores, classifica-os e salva um novo arquivo.
    """
    # Ler o arquivo de entrada
    df = pd.read_csv(arquivo_entrada)

    # Verificar se as colunas dos fatores existem
    colunas_fatores = ["Ansiedade", "Depressão", "Autoeficácia"]
    for coluna in colunas_fatores:
        if coluna not in df.columns:
            raise ValueError(f"A coluna '{coluna}' não foi encontrada no arquivo.")

    # Criar uma coluna para classificação de cada fator
    for coluna in colunas_fatores:
        df[f"Classificação {coluna}"] = df[coluna].apply(classificar_pontuacao)

    # Salvar o resultado em um novo arquivo CSV
    df[colunas_fatores + [f"Classificação {coluna}" for coluna in colunas_fatores]].to_csv(arquivo_saida, index=False)
    print(f"Resultados com classificação salvos em '{arquivo_saida}'.")

# Arquivos de entrada e saída
arquivo_entrada = "Fatores_Atualizados.csv"
arquivo_saida = "fatores_classificados.csv"

# Processar e salvar o arquivo classificado
processar_fatores_para_ranqueamento(arquivo_entrada, arquivo_saida)
