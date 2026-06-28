import os
import pandas as pd
from scipy.stats import pearsonr

# Caminho da pasta com os arquivos
input_folder = 'Dados_Fatores'
output_folder = 'Resultados_Pearson'

# Criar a pasta de saída, caso não exista
os.makedirs(output_folder, exist_ok=True)

# Listar todos os arquivos CSV na pasta de entrada
files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Colunas do EAISR-E e fatores
eaisre_columns = [
    "Vejo a rede social muitas vezes todos os dias",
    "Compartilho fotos e vídeos em redes sociais com frequência.",
    "Existem contas de redes sociais (blogs) que eu sigo constantemente.",
    "Eu tenho mais de uma conta de rede social que uso ativamente.",
    "Eu acho que as redes sociais são muito úteis.",
    "Eu gosto de acompanhar as ações dos meus amigos nas redes sociais.",
    "Costumo conferir o que meus amigos fazem nas redes sociais.",
    "Sinto-me mais confortável nas redes sociais do que quando estou em ambientes sociais (com outras pessoas).",
    "Eu prefiro redes sociais em vez de gastar tempo com meu círculo social.",
    "Eu posso me expressar mais claramente usando redes sociais.",
    "Eu prefiro usar redes sociais do que telefonar quando estou me comunicando com amigos.",
    "Eu uso redes sociais principalmente para amizades e conversas.",
    "Eu frequentemente atualizo meu perfil nas redes sociais."
]
fatores_columns = ["Ansiedade", "Depressão", "Autoeficácia"]

# Processar cada arquivo
for file in files:
    # Carregar o arquivo
    file_path = os.path.join(input_folder, file)
    data = pd.read_csv(file_path)

    # Calcular as correlações
    correlation_results = []
    for eaisre_col in eaisre_columns:
        for fator_col in fatores_columns:
            correlation, p_value = pearsonr(data[eaisre_col], data[fator_col])
            correlation_results.append({
                "Pergunta_EAISR-E": eaisre_col,
                "Fator_QSG-12": fator_col,
                "Correlacao": correlation,
                "P_Valor": p_value
            })

    # Criar DataFrame com os resultados
    correlation_df = pd.DataFrame(correlation_results)

    # Salvar o arquivo com os resultados
    output_file = os.path.join(output_folder, file.replace('.csv', '_pearson.csv'))
    correlation_df.to_csv(output_file, index=False)

# Mensagem de finalização
print(f"Análise concluída. Resultados salvos na pasta: {output_folder}")
