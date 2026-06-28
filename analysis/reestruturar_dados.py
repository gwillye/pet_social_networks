import pandas as pd

# Caminho para o arquivo enviado
input_file = 'dados_organizar_final.csv'
output_file = 'dados_reestruturados_final.csv'

# Carregar o arquivo CSV
data = pd.read_csv(input_file)

# Reestruturar o DataFrame
restructured_data = data.pivot(
    index="Pergunta_EAISR-E",
    columns="Fator_QSG-12",
    values=["Correlacao", "P_Valor"]
)

# Flattenar o MultiIndex para simplificar o cabeçalho
restructured_data.columns = [
    f"{col[1]}_{col[0]}" for col in restructured_data.columns
]

# Resetar o índice para salvar em formato tabular
restructured_data.reset_index(inplace=True)

# Salvar o arquivo reestruturado
restructured_data.to_csv(output_file, index=False)