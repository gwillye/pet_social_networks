import pandas as pd
from scipy.stats import pearsonr

# Caminhos dos arquivos
eaisre_file = 'eaisre.csv'
fatores_file = 'Fatores_Atualizados.csv'
output_file = 'correlacao_geral.csv'

# Carregar os arquivos
eaisre_data = pd.read_csv(eaisre_file)
fatores_data = pd.read_csv(fatores_file)

# Selecionar as colunas relevantes
eaisre_columns = eaisre_data.columns.tolist()
fatores_columns = ['Ansiedade', 'Depressão', 'Autoeficácia']

# Calcular as correlações de Pearson
correlation_results = []

for eaisre_col in eaisre_columns:
    for fator_col in fatores_columns:
        correlation, p_value = pearsonr(eaisre_data[eaisre_col], fatores_data[fator_col])
        correlation_results.append({
            "Pergunta_EAISR-E": eaisre_col,
            "Fator_QSG-12": fator_col,
            "Correlacao": correlation,
            "P_Valor": p_value
        })

# Criar DataFrame com os resultados
correlation_df = pd.DataFrame(correlation_results)

# Salvar o arquivo com os resultados
correlation_df.to_csv(output_file, index=False)
