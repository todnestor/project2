#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y

sns.set()
samples=np.random.binomial(60,0.1,size=10000)
x,y = ecdf(samples)
_=plt.plot(x,y,marker='.', linestyle='none')
plt.margins(0.02)
_=plt.xlabel('number of successes')
_=plt.ylabel('CDF')
plt.show()
