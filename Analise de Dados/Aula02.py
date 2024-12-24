import numpy as np
import pandas as pd

houses_sp = pd.read_csv('houses_sp.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

houses_sp = houses_sp.drop(columns=['city'])

#print(houses_sp['rooms'].median())

#transforma os dados errados da coluna rooms na media de rooms do banco !! não é ideal usar este metodo, porem melhor que deletar o elemento da lista !!
houses_sp['rooms'] = houses_sp['rooms'].fillna(houses_sp['rooms'].median())

#transforma os dados errados da coluna floor '-' para '0', tendo em vista que o - significa que é um casa.
houses_sp.loc[houses_sp['floor'] == '-', 'floor'] = '0'

print(houses_sp.head())