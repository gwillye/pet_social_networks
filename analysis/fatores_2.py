import pandas as pd

# Caminho para o arquivo CSV
file_path = 'Fatores.csv'

# Carregar os dados do CSV
data = pd.read_csv(file_path)

# Definir os itens negativos (que devem ser invertidos)
negative_items = [
    "Suas preocupações lhe têm feito perder muito sono?",  # Item 2
    "Tem notado que está constantemente agoniado e tenso?",  # Item 5
    "Tem tido a sensação de que não pode superar suas dificuldades?",  # Item 6
    "Tem se sentido pouco feliz e deprimido(a)?",  # Item 9
    "Tem perdido confiança em si mesmo?",  # Item 10
    "Tem pensado que você é uma pessoa que não serve para nada?"  # Item 11
]

# Itens pertencentes a cada fator
depression_items = [
    "Sente-se razoavelmente feliz considerando todas as circunstâncias?",  # Item 12
    "Tem sido capaz de enfrentar adequadamente os seus problemas?",  # Item 8
    "Tem se sentido capaz de tomar decisões?",  # Item 4
    "Tem sido capaz de desfrutar suas atividades normais de cada dia?",  # Item 7
    "Tem podido concentrar-se bem no que faz?"  # Item 1
]

anxiety_items = [
    "Suas preocupações lhe têm feito perder muito sono?",  # Item 2
    "Tem se sentido pouco feliz e deprimido(a)?",  # Item 9
    "Tem notado que está constantemente agoniado e tenso?"  # Item 5
]

self_efficacy_items = [
    "Tem se sentido capaz de tomar decisões?",  # Item 4
    "Tem pensado que você é uma pessoa que não serve para nada?",  # Item 11
    "Tem perdido confiança em si mesmo?",  # Item 10
    "Tem sentido que tem um papel útil na vida?",  # Item 3
    "Tem tido a sensação de que não pode superar suas dificuldades?"  # Item 6
]

# Inverter as pontuações dos itens negativos
for item in negative_items:
    if item in data.columns:
        data[item] = 5 - data[item]

# Calcular as pontuações dos fatores
data['Depressão'] = data[depression_items].sum(axis=1)
data['Ansiedade'] = data[anxiety_items].sum(axis=1)
data['Autoeficácia'] = data[self_efficacy_items].sum(axis=1)

# Salvar o arquivo atualizado
output_file = 'Fatores_Atualizados.csv'
data.to_csv(output_file, index=False)