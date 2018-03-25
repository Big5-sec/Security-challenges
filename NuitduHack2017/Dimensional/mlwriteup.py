import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

Q = pd.DataFrame.from_csv("./flag.csv")
K = pd.DataFrame(PCA(2).fit_transform(Q.values))
K.plot.scatter(x=0,y=1,figsize=(12, 8))
plt.axis('equal')
plt.show()

