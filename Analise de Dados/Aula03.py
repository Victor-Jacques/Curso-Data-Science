import pandas as pd
import webbrowser
import numpy as np

houses = pd.read_csv('houses_to_rent.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#houses.describe().to_html("dataframe.html")
#print(houses['bathroom'].value_counts())

#webbrowser.open("dataframe.html")

q1 = houses['bathroom'].quantile(0.25)
q3 = houses['bathroom'].quantile(0.75)

IQR = q3 - q1
#filtro dos outliers, q3 busca os pontos fora da curva
houses_outliers = houses[(houses['bathroom'] < q1 - (IQR * 1.5)) | (houses['bathroom'] > q3 + (IQR * 1.5))]

#filtro dos inliers, é o inverso dos outliers
houses_inliers = houses[(houses['bathroom'] >= q1 - (IQR * 1.5)) & (houses['bathroom'] <= q3 + (IQR * 1.5))]


houses_outliers.describe().to_html("describeOutliers.html")
#webbrowser.open("describeOutliers.html")
print((q1 - (IQR * 1.5)), (q3 + (IQR * 1.5)))