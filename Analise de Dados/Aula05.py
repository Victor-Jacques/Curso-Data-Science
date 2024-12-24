import seaborn as sns
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

candy = pd.read_csv('candy_production.csv')

candy['observation_date'] = pd.to_datetime(candy['observation_date'])

print(candy.info())

# candy.plot(x='observation_date', y='industrial_production')
candy_filtered = candy[candy['observation_date'] >= '2010-01-01']
ax = candy_filtered.plot(x='observation_date', y='industrial_production', figsize=(12,6))
xcoords = ['2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01']

for xc in xcoords:
    plt.axvline(x=xc, color='black', linestyle='--')


plt.show()