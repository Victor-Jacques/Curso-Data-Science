import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser as wb


penguins = sns.load_dataset("penguins")

# print(penguins['species'].value_counts())

# for col in penguins.drop(columns=['species', 'island', 'sex']):
#     sns.barplot(data=penguins, x='species', y=col, ci=90)

#sns.scatterplot(x='body_mass_g', y='bill_length_mm', hue='species', data=penguins)
sns.pairplot(data=penguins, hue='species')
plt.show()

# wb.open('PenguinsGraficos.html')