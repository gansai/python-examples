import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


# Create a timeseries data randomly
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2000',
                                   periods=1000))
ts = ts.cumsum()

ts.plot()

plt.show()

df = pd.DataFrame(np.random.randn(1000,2), columns=['a','b'])

df.plot(kind='hexbin', x='a', y='b', gridsize=25)

plt.show()

