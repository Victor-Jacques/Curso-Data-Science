import seaborn as sns
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')

# print(iris['species'].value_counts())
col = 'sepal_length'
grafico = sns.histplot(data=iris, x='sepal_length', kde=True).set_title(f"Distribuição da variável {col}")
# grafico.to_html("grafico.html")
# webbrowser.open("grafico.html")
for col in iris.drop(columns='species'):
    sns.barplot(data=iris, x=iris['species'], hue=iris['species'], y = col, ci = 90).set_title(f'Distribuição da variável {col}')
    plt.show()

