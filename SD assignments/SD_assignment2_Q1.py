import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_rows = None
pd.options.display.float_format = '{:.2f}'.format

df = pd.DataFrame()

df['year'] = [i for i in range(2010, 2022)]
df['income'] = [102, 222, 322, 123, 234, 455, 554, 433, 234, 345, 234, 444]
df['consum'] = [73, 166, 229, 89, 187, 330, 424, 310, 188, 274, 200, 351]

sf = 0
x_axis = []
sse = []

while sf <= 1:
    df['consum_sim'] = (1 - sf) * df['income']
    df['error'] = df['consum'] - df['consum_sim']
    df['sqr_err'] = np.power(df['error'], 2)
    x_axis.append(sf)
    sse.append(np.sum(df['sqr_err']))
    df.drop(['consum_sim', 'error', 'sqr_err'], axis=1)
    sf += 0.01

opt_error = np.min(sse)
sf_optimal = x_axis[sse.index(opt_error)]

print('Optimal values of SSE = {}'.format(opt_error))
print('Optimal values of SF that got optimal SSE = {}'.format(sf_optimal))

plt.plot(x_axis, sse)
plt.xlabel('SF values')
plt.ylabel('SSE value')
plt.title('SSE optimal = ' + str(opt_error) + '\nSF got optimal = ' + str(sf_optimal))
plt.show()
