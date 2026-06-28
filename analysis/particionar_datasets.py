import pandas as pd

# Carregar o dataset original
dataset = pd.read_csv('dataset_fatores_final.csv')

# Converter a coluna 'Qual sua idade?' para numérico, ignorando erros (caso haja valores inválidos)
dataset['Qual sua idade?'] = pd.to_numeric(dataset['Qual sua idade?'], errors='coerce')

# Separar por sexo
homens = dataset[dataset['Qual seu sexo?'] == 'Homem']
mulheres = dataset[dataset['Qual seu sexo?'] == 'Mulher']

# Salvar datasets por sexo
homens.to_csv('homens.csv', index=False)
mulheres.to_csv('mulheres.csv', index=False)

# Separar por idade
idade_sub21 = dataset[dataset['Qual sua idade?'] <= 21]
idade_sub26 = dataset[(dataset['Qual sua idade?'] > 21) & (dataset['Qual sua idade?'] <= 26)]
idade_over27 = dataset[dataset['Qual sua idade?'] >= 27]

# Salvar datasets por idade
idade_sub21.to_csv('idade_sub21.csv', index=False)
idade_sub26.to_csv('idade_sub26.csv', index=False)
idade_over27.to_csv('idade_over27.csv', index=False)

# Convertendo a coluna 'Qual seu MGA (Média Geral Acadêmica)?' para numérico
dataset['Qual seu MGA (Média Geral Acadêmica)?'] = pd.to_numeric(dataset['Qual seu MGA (Média Geral Acadêmica)?'], errors='coerce')

# Particionamento por MGA
under_mga = dataset[dataset['Qual seu MGA (Média Geral Acadêmica)?'] < 6]
over_mga = dataset[dataset['Qual seu MGA (Média Geral Acadêmica)?'] >= 6]

# Salvando os datasets MGA
under_mga.to_csv('under_mga.csv', index=False)
over_mga.to_csv('over_mga.csv', index=False)

# Particionamento por semestre
dataset['Qual semestre você está cursando?'] = pd.to_numeric(dataset['Qual semestre você está cursando?'], errors='coerce')
inicio_curso = dataset[dataset['Qual semestre você está cursando?'] <= 4]
fim_curso = dataset[(dataset['Qual semestre você está cursando?'] > 4) & (dataset['Qual semestre você está cursando?'] <= 8)]
over_curso = dataset[dataset['Qual semestre você está cursando?'] > 8]

# Salvando os datasets de semestre
inicio_curso.to_csv('inicio_curso.csv', index=False)
fim_curso.to_csv('fim_curso.csv', index=False)
over_curso.to_csv('over_curso.csv', index=False)

# Particionamento por curso
cursos = dataset['Qual seu curso?'].unique()
for curso in cursos:
    curso_df = dataset[dataset['Qual seu curso?'] == curso]
    curso_df.to_csv(f'{curso}.csv', index=False)

# Particionamento por tempo em redes sociais
tempos_redes_sociais = dataset['Quanto tempo em média você passa em redes sociais diariamente?'].unique()
for tempo in tempos_redes_sociais:
    tempo_df = dataset[dataset['Quanto tempo em média você passa em redes sociais diariamente?'] == tempo]
    tempo_df.to_csv(f'tempo_{tempo.replace(" ", "_")}.csv', index=False)

print("Particionamento realizado e arquivos salvos com sucesso.")
