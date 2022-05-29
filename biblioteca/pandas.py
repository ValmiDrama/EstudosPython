import pandas as pd

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

lista_produtos = [['laptop', 'impressora', 'tablet', 'mesa', 'cadeira'],[1300, 150, 300, 450, 200]]
df = pd.DataFrame(lista_produtos).transpose()
df.columns = ['Produto', 'Valor']
print(df)