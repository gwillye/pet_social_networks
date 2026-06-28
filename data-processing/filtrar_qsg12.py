import pandas as pd

dataset = pd.read_csv('dataset.csv')

colunas_relevantes = [
        'Tem podido concentrar-se bem no que faz?',
        'Suas preocupações lhe têm feito perder muito sono?',
        'Tem sentido que tem um papel útil na vida?',
        'Tem se sentido capaz de tomar decisões?',
        'Tem notado que está constantemente agoniado e tenso?',
        'Tem tido a sensação de que não pode superar suas dificuldades?',
        'Tem se sentido pouco feliz e deprimido(a)?',
        'Tem sido capaz de enfrentar adequadamente os seus problemas?',
        'Tem sido capaz de desfrutar suas atividades normais de cada dia?',
        'Tem perdido confiança em si mesmo?','Tem pensado que você é uma pessoa que não serve para nada?',
        'Sente-se razoavelmente feliz considerando todas as circunstâncias?'
]

eaisre_dataset = dataset[colunas_relevantes]
eaisre_dataset.to_csv('qsg12.csv', index=False)


