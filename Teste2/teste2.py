import pandas as pd
import tabula
from tabula import read_pdf

listArquivo = tabula.read_pdf('./arquivo.pdf', pages='5')
print(len(listArquivo))
print(listArquivo)







# #Obs.: Pula pagina 1,2,3 inicia na Pagina 4 e 5 1 tabela.
# list_Header = []

# # Pegar primeira tabela
# tabela_de_indice_0 = []



# # Tirar Cabecario HEAD
# list_Header = tabela_de_indice_0

