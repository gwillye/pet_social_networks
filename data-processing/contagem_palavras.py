def contar_palavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()
        
        # Remove pontuação e transforma em minúsculas
        texto = texto.lower()
        pontuacao = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in pontuacao:
            texto = texto.replace(char, " ")
        
        # Separa as palavras
        palavras = texto.split()
        
        # Conta a frequência de cada palavra
        contagem_palavras = {}
        for palavra in palavras:
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1
        
        # Exibe a contagem de cada palavra
        for palavra, contagem in contagem_palavras.items():
            print(f'{palavra}: {contagem}')
    
    except FileNotFoundError:
        print(f'O arquivo {arquivo} não foi encontrado.')

# Chame a função com o nome do arquivo
contar_palavras('dados.txt')
