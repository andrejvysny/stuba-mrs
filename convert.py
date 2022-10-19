import scipy.io
import pandas as pd

name = 'vystup4'
mat = scipy.io.loadmat( name + '.mat')


df = pd.DataFrame(mat[name])
df.to_csv(name + '.csv')