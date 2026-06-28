import pandas as pd

# Função para formatar números
def formatar_numero(valor):
    try:
        # Converter o valor para float
        numero = float(valor)
        # Formatar para manter apenas os dois primeiros dígitos
        # Primeiro, vamos multiplicar por 100 e truncar para manter os dois primeiros dígitos
        if numero < 0:
            # Se o número for negativo, ajusta o sinal após truncar
            return -1 * (int(abs(numero) * 100) / 100.0)
        else:
            return int(numero * 100) / 100.0
    except ValueError:
        # Retornar o valor original se não for um número válido
        return valor

# Ler o arquivo CSV
nome_arquivo = 'correlacao_spearman.csv'
df = pd.read_csv(nome_arquivo)

# Aplicar a formatação em cada valor do DataFrame
df_formatado = df.applymap(formatar_numero)

# Salvar o resultado em um novo arquivo CSV
df_formatado.to_csv('correlacao_spearman.csv', index=False)

print("Arquivo CSV formatado com sucesso!")
