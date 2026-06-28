import pandas as pd

# Caminhos dos arquivos
fatores_file = 'Fatores_Atualizados.csv'
dataset_file = 'dataset.csv'
output_file = 'dataset_fatores_final.csv'

# Carregar os arquivos
fatores_data = pd.read_csv(fatores_file)
dataset_data = pd.read_csv(dataset_file)

# Selecionar as últimas três colunas de Fatores_Atualizados.csv
fatores_last_three_cols = fatores_data.iloc[:, -3:]

# Concatenar os arquivos
final_dataset = pd.concat([dataset_data, fatores_last_three_cols], axis=1)

# Salvar o novo arquivo
final_dataset.to_csv(output_file, index=False)