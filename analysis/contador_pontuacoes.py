import pandas as pd

def contar_classificacoes(arquivo_csv):
    """
    Lê um arquivo CSV com colunas de classificação para fatores e conta as classificações para cada fator.
    
    Parâmetros:
        arquivo_csv (str): Caminho para o arquivo CSV.

    Retorno:
        dict: Um dicionário com as contagens de classificações para cada fator.
    """
    # Carregar o arquivo CSV
    df = pd.read_csv(arquivo_csv)

    # Identificar as colunas de classificação
    colunas_classificacao = [col for col in df.columns if col.startswith("Classificação")]

    # Contar as classificações para cada fator
    contagens = {}
    for coluna in colunas_classificacao:
        fator = coluna.replace("Classificação ", "")
        contagens[fator] = df[coluna].value_counts().to_dict()

    return contagens

def salvar_resultados(contagens, arquivo_saida):
    """
    Salva as contagens de classificações em um arquivo CSV.

    Parâmetros:
        contagens (dict): Dicionário com as contagens de classificações.
        arquivo_saida (str): Caminho para salvar o arquivo CSV.
    """
    # Converter o dicionário em um DataFrame
    df_resultado = pd.DataFrame(contagens).fillna(0).astype(int)

    # Salvar no arquivo CSV
    df_resultado.to_csv(arquivo_saida, index_label="Classificação")
    print(f"Resultados salvos em '{arquivo_saida}'.")

# Caminho do arquivo CSV de entrada
arquivo_entrada = "fatores_classificados.csv"

# Caminho do arquivo CSV de saída
arquivo_saida = "contagem_classificacoes.csv"

# Processar e salvar os resultados
contagens = contar_classificacoes(arquivo_entrada)
salvar_resultados(contagens, arquivo_saida)
