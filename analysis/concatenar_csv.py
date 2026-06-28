import os
import pandas as pd

# Função para concatenar os CSVs de uma pasta específica
def concatenar_csvs(pasta, output_csv):
    # Lista para armazenar todos os DataFrames lidos
    dataframes = []
    
    # Caminho completo da pasta
    caminho_pasta = f'./{pasta}'
    
    # Listar todos os arquivos CSV na pasta
    arquivos_csv = [f for f in os.listdir(caminho_pasta) if f.endswith('.csv')]
    
    # Iterar sobre os arquivos CSV e concatenar
    for arquivo in arquivos_csv:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        print(f"Lendo arquivo: {caminho_arquivo}")
        
        # Ler o CSV e adicionar à lista de DataFrames
        df = pd.read_csv(caminho_arquivo)
        dataframes.append(df)
    
    # Concatenar todos os DataFrames em um único
    df_concatenado = pd.concat(dataframes, ignore_index=True)
    
    # Salvar o DataFrame concatenado em um arquivo CSV
    df_concatenado.to_csv(output_csv, index=False)
    print(f"Arquivo concatenado salvo como: {output_csv}")

# Concatenar arquivos CSV nas pastas 'Kendall', 'Pearson' e 'Spearman'
concatenar_csvs('Resultados_Pearson/', 'correlacao_pearson.csv')