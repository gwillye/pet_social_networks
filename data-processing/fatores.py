import pandas as pd

# Função para converter as respostas de texto para uma escala numérica
def converter_resposta(resposta):
    if resposta in ['Mais que o de costume', 'Muito mais que o de costume']:
        return 1
    elif resposta in ['Igual ao de costume']:
        return 2
    elif resposta in ['Menos que o de costume']:
        return 3
    elif resposta in ['Muito menos que o de costume']:
        return 4
    elif resposta in ['Não, de modo algum']:
        return 1
    elif resposta in ['Não mais que o costume']:
        return 2
    elif resposta in ['Um pouco mais do que o costume']:
        return 3
    else:
        return 4

# Função para calcular os fatores com base nas respostas
def calcular_fatores(respostas):
    # Definir as perguntas de cada fator
    perguntas_depressao = [3, 4, 7, 8, 9, 12]  # Perguntas relacionadas à depressão
    perguntas_ansiedade = [2, 5, 6]            # Perguntas relacionadas à ansiedade
    perguntas_autoeficacia = [1, 10, 11]       # Perguntas relacionadas à autoeficácia
    
    # Extrair as respostas para cada fator
    respostas_depressao = [respostas[i-1] for i in perguntas_depressao]
    respostas_ansiedade = [respostas[i-1] for i in perguntas_ansiedade]
    respostas_autoeficacia = [respostas[i-1] for i in perguntas_autoeficacia]
    
    # Somar as respostas
    fator_depressao = sum(respostas_depressao)
    fator_ansiedade = sum(respostas_ansiedade)
    fator_autoeficacia = sum(respostas_autoeficacia)
    
    return fator_depressao, fator_ansiedade, fator_autoeficacia

# Função para processar o CSV e calcular os fatores
def processar_csv(arquivo_entrada, arquivo_saida):
    # Ler o CSV
    df = pd.read_csv(arquivo_entrada)
    
    # Adicionar novas colunas para os resultados dos fatores
    df['Fator_Depressao'] = 0
    df['Fator_Ansiedade'] = 0
    df['Fator_Autoeficacia'] = 0
    
    # Iterar sobre cada linha do CSV
    for index, row in df.iterrows():
        # Coletar as respostas como uma lista
        respostas = [
            converter_resposta(row['Tem podido concentrar-se bem no que faz?']),
            converter_resposta(row['Suas preocupações lhe têm feito perder muito sono?']),
            converter_resposta(row['Tem sentido que tem um papel útil na vida?']),
            converter_resposta(row['Tem se sentido capaz de tomar decisões?']),
            converter_resposta(row['Tem notado que está constantemente agoniado e tenso?']),
            converter_resposta(row['Tem tido a sensação de que não pode superar suas dificuldades?']),
            converter_resposta(row['Tem sido capaz de enfrentar adequadamente os seus problemas?']),
            converter_resposta(row['Tem sido capaz de desfrutar suas atividades normais de cada dia?']),
            converter_resposta(row['Tem perdido confiança em si mesmo?']),
            converter_resposta(row['Tem pensado que você é uma pessoa que não serve para nada?']),
            converter_resposta(row['Sente-se razoavelmente feliz considerando todas as circunstâncias?']),
        ]
        
        # Calcular os fatores
        fator_depressao, fator_ansiedade, fator_autoeficacia = calcular_fatores(respostas)
        
        # Adicionar os fatores ao DataFrame
        df.at[index, 'Fator_Depressao'] = fator_depressao
        df.at[index, 'Fator_Ansiedade'] = fator_ansiedade
        df.at[index, 'Fator_Autoeficacia'] = fator_autoeficacia
    
    # Salvar o arquivo CSV com as novas colunas
    df.to_csv(arquivo_saida, index=False)
    print(f"Arquivo processado e salvo como {arquivo_saida}")

# Nome do arquivo de entrada e saída
arquivo_entrada = 'dataset_normalizado.csv'
arquivo_saida = 'dataset_com_fatores.csv'

# Executar o processamento
processar_csv(arquivo_entrada, arquivo_saida)
