import pandas as pd

def atualizar_csv(primeiro_csv, segundo_csv, saida_csv):
    # Leitura dos dois datasets
    df_primeiro = pd.read_csv(primeiro_csv)
    df_segundo = pd.read_csv(segundo_csv)

    # Encontrar colunas comuns entre os dois CSVs
    colunas_comuns = df_primeiro.columns.intersection(df_segundo.columns)

    # Atualizar os dados do primeiro CSV com os dados do segundo CSV onde as colunas correspondem
    for coluna in colunas_comuns:
        df_primeiro[coluna] = df_segundo[coluna]

    # Salvar o CSV atualizado
    df_primeiro.to_csv(saida_csv, index=False)
    print(f"CSV atualizado salvo como '{saida_csv}'.")

# Exemplo de uso
atualizar_csv('sist_inf.csv', 'dataset_normalizado_qsg12.csv', 'sist_inf.csv')
