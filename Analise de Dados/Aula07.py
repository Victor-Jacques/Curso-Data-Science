import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser as wb
import numpy as np

df = pd.read_csv('winequality-red.csv')
#Numero de linhas e colunas
# print(df.shape)

#Tipos dos dados
# print(df.dtypes)

#verificar se há dados nulos
# print(df.info())

# df_desc = df.describe()
# df_desc.loc["IQR"] = df_desc.loc["75%"] - df_desc.loc["25%"]
# df_desc.to_html('WineIQR.html')

#Verificar se há outliers
# for col in df:
#     sns.histplot(data=df, x=col, kde=True).set_title(f"Distribuição da variável {col}")
#     plt.show()

#Verifica cada coluna, se há outliers e retorna os indices de cada outlier encontrado das respectivas colunas
#Metodo do Quartil

# for col in df.drop(columns='quality'):
#
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1
#
#     aux_outliers = df[(df[col] < Q1 - (IQR * 1.5))
#                     | (df[col] > Q3 + (IQR * 1.5))]
#
#     indices_outliers = aux_outliers.index.tolist()
#
#     if len(indices_outliers) >= 1:
#         print(f"A coluna {col} tem {len(indices_outliers)} outliers!")
#         print("\nOs indices deles são:\n")
#         print(indices_outliers)
#
#     else:
#         print(f"A coluna {col} não tem outliers!")
#
#     print()
#     print("="*80)
#     print()

#Verifica a qualidade dos vinhos
# print(df['quality'].value_counts(normalize=True))

# print((df['quality'].describe()))
#
# sns.histplot(data=df, x='quality', kde=True)
# plt.show()

# df.corr().to_html("WineCorr.html")
# wb.open("WineCorr.html")

# plt.figure(figsize=(12,6))
#
# sns.heatmap(df.corr(), annot=True)
# plt.show()

#É identificado que as caracteristicas com mais influencia sao as 3 ultimas: citric_acid, sulphates e alcohol
#E as 2 primeiras: volatile_acidity e total_sulfur_dioxide
#print(df.corr()['quality'].sort_values())

#Calculo para a visualização do intervalo de confiança de 90% para a media de cada uma das variaveis fisico-quimicas
# for col in df.drop(columns='quality'):
#     sns.barplot(data=df, x='quality', y=col, errorbar=('ci', 90), hue='quality')
#     plt.show()

#Alteração da qualidade para Bom ou Ruim
df['quality_bin'] = df['quality'].apply(lambda x : "bom" if x > 5 else "ruim")
df_bin = df.drop(columns=['quality'])
# df_bin.to_html("WineBOMouRUIM.html")
# wb.open("WineBOMouRUIM.html")

# df_bin.to_csv('winequality-red-binary.csv', index=False)

# print(df_bin)

#Varredura nas variaveis para ver se é possivel achar alguma caracteristica que diga se o vinho é bom ou ruim
for col in df_bin.drop(columns='quality_bin'):
    sns.histplot(data=df_bin, x=col, kde=True, hue=df_bin['quality_bin']).set_title(f"Distribuição da variável {col}")
    plt.show()

#Assim é possivel notar que há algumas variáveis que parecem ajudar a separar a qualidade do vinho
#Com mais eficiencia agora que o problema foi mudado para binario