import pandas as pd

import tabula

#--------------------------------#
#            Pandas
#--------------------------------#

#obs: DataFrame é uma estrutura de dados bidimensional com os dados alinhados
#     de forma tabular em linhas e colunas, mutável em tamanho e potencialmente 
#     heterogênea, semelhantemente a uma pasta de trabalho do MS-EXCEL.

list =['Dado A1', 'Dado A2']
list2 =['Dado B1', 'Dado B2']
lisList = [list, list2]
print(len(list))

#TODO Convert a List

# 
# df = pd.DataFrame (list, columns=['Coluna'])
# print(df)

# print(list)

#TODO Convert a List of Lists

# df = pd.DataFrame(lisList, columns=['COLUNAS 1', 'COLUNA 2'])
# print(df)

#TODO Convert a List of Lists transposta

lista_produtos = [['laptop', 'impressora', 'tablet', 'mesa', 'cadeira'],[1300, 200, 300, '', 200]]
lista_produtos2 = [['notebook', 'celular', 'geladeira', 'fogao', 'microondas'],[2300, '', 1300, 650, 200]]
df = pd.DataFrame(lista_produtos).transpose()
df2 = pd.DataFrame(lista_produtos2).transpose()
df.columns = ['Produto', 'Valor']
df2.columns = ['Produto', 'Valor']
# print(df)
# print(df2)


# #! METODOS
# # head(int) Exibe numero X de linhas
# print(df.head(1))

# # shape
# print(df.shape)

# # describe() - resumo numerico + statisticas
# print(df.describe())

# #unica coluna COLUNA = DataFrame['COL NAME'] ou DataFrame[['COL NAME', COL ID]]
# coluna1 = df['Produto']
# coluna2 = df[['Produto', 'Valor']]
# print('')
# print(coluna1)
# print('')
# print(coluna2)
# print('')

# # Metodo .loc DataFrame.loc[indice] ou DataFrame.loc[indiceInicial:indicefinal]

# linha1 = df.loc[1]
# linha1a3 = df.loc[1:3]
# print(linha1)
# print(linha1a3)

# # Obs: .loc condicional todas as linhas onde COL ID == VALOR NA LINHA
# #   linhaCondicao = df.loc[df['COL ID'] == 'VALOR NA LINHA']

# # .loc Linha e Colunas 
# # df.loc[df['COL ID'] == 'VALOR COL'], ['LINHA ID', 'NOME', 'DESCRI']
# # exemplo:

# linha_col_df = df.loc[df['Produto'] == 'mesa', ['Produto', 'Valor']]
# print(linha_col_df)

# # Add COLUNA NOVA 
# # df.loc['Estoque'] =''
# df.loc[:,'Estoque'] = 2
# # Obs. ':' =  todas linhas ou colunas.
# # COluna ESTOQUE, :(todas) linhas = 0

# # ADD COL UMA QUE EXISTE
# df['Val 10x'] = df['Valor']*10
# print(df)
  
# #  append(ARQUIVO) - Junta dois DataFrame Linhas, Podendo ser adicionado mais de 1x, (duplicidade)
# df = df.append(df2)
# print(df)

# # Exluir - Obs. sempre por o AXIS=1 COL -> AXIS=0 -> LINHA
# dfExcluida = df.drop(0, axis=1)
# print(df)
# print(dfExcluida)

# #  Exlui todas linha com pelo menos 1 valor 'NaN'
# dfDel = df.dropna()

# # Preencher 'NaN', com valor ou valor medio df['Valor'].mean()
# print(df)
# df['Valor'] = df['Valor'].fillnad(df['Valor'].mean())
# print(df)

# # Preenche campo vazio da coluna com ultimo valor df.ffill()
# df=df.ffill()

# #  Contas os itens de uma COluna
# ContarCol = df['COL'].value_counts()

# # Agrupa por VALOR e SUM os numeros
# dfGroup = df.groupby('Valor').sum()

# # MesclaTabelas
# df = df.merge(df2) sendo que df e df2 tem 1 coluna em comun.

#TODO Panda

# teste_dicionario = {'Nascimento': ['01.12', '12.01'], 'valor': ['36', '63'], 'nome': ['Jr', 'Rj'], 'produto': ['22', '33'],}

# # teste_dataFrame = pd.DataFrame(teste_dicionario)

# print(teste_dicionario)


# #TODO Importa arquivo
# arquivo = tabula.read_pdf("arquivo.pdf", pages="5")

# #TODO Converte PDF para CVS arquivo

# tabula.convert_into("arquivo.pdf", "arquivo.csv", output_format="csv", pages="5")

# #TODO Converte PDF para CVS arquivo

# #TODO Converte PDF para CVS arquivo
# https://insightlab.ufc.br/6-truques-do-pandas-para-impulsionar-sua-analise-de-dados
# 6 truques do Pandas para impulsionar sua análise de dados
# Selecione colunas por tipos de dados
# Converta sequências de caracteres em números
# Detectar e manipular valores ausentes
# Converta um recurso numérico contínuo em um recurso categórico
# Crie um DataFrame a partir da área de transferência
# Crie um DataFrame a partir de vários arquivos


