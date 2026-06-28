import pandas as pd

dataset = pd.read_csv('dataset.csv')

colunas_relevantes = [
        'Vejo a rede social muitas vezes todos os dias',
        'Compartilho fotos e vídeos em redes sociais com frequência.',
        'Existem contas de redes sociais (blogs) que eu sigo constantemente.',
        ' Eu tenho mais de uma conta de rede social que uso ativamente.',
        'Eu acho que as redes sociais são muito úteis.',
        'Eu gosto de acompanhar as ações dos meus amigos nas redes sociais.',
        'Costumo conferir o que meus amigos fazem nas redes sociais.',
        'Sinto-me mais confortável nas redes sociais do que quando estou em ambientes sociais (com outras pessoas).',
        'Eu prefiro redes sociais em vez de gastar tempo com meu círculo social.',
        'Eu posso me expressar mais claramente usando redes sociais.',
        'Eu prefiro usar redes sociais do que telefonar quando estou me comunicando com amigos.',
        ' Eu uso redes sociais principalmente para amizades e conversas.',
        'Eu frequentemente atualizo meu perfil nas redes sociais.'
]

eaisre_dataset = dataset[colunas_relevantes]
eaisre_dataset.to_csv('eaisre.csv', index=False)