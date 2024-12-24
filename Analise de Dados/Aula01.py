import numpy as np
import pandas as pd
from pandas import value_counts

cuisine_rating = pd.read_csv('Cuisine_rating.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#print(cuisine_rating.head())

#cuisine_rating.info()

#print(cuisine_rating['Cuisines'].value_counts()) #Conta a frequencia que aparece cada culinaria
#mean() calcula a media
#print(cuisine_rating[cuisine_rating['Cuisines'] == 'Japanese']['Overall Rating'].mean())
#print(cuisine_rating[cuisine_rating['YOB'] > 2000]) Busca no banco de dados todos que nasceram apos os anos 2000

#print(cuisine_rating['Location'].value_counts())

#seleciona apenas os dados numericos e os transforma em uma lista
numeric_cols = cuisine_rating.select_dtypes(include=np.number).columns.to_list()

#retorna a media das colunas baseados pela localizacao
# print(cuisine_rating.groupby(['Location'])[numeric_cols].mean())

#retorna a media das colunas por localizacao e tipo de culinaria
print(cuisine_rating.groupby(['Location', 'Cuisines'])[numeric_cols].mean())