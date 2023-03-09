import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.width = None
pd.options.display.max_rows = None
pd.options.display.float_format = '{:.2f}'.format

df = pd.DataFrame()

df['year'] = [i for i in range(2010, 2022)]
df['price'] = [101, 90, 99, 123, 111, 98, 109, 104, 91, 122, 116, 109]
df['demand'] = [1005, 1154, 1033, 777, 876, 1046, 904, 958, 1144, 792, 828, 913]

rd = 500
e = -2
sse = []
x_axis = []
y_axis = []

while rd <= 1500:

    while e <= -1:
        df['demand_sim'] = rd * np.power((df['price'] / 100), e)
        df['error'] = df['demand'] - df['demand_sim']
        df['sqr_err'] = np.power(df['error'], 2)
        x_axis.append(e)
        y_axis.append(rd)
        sse.append(np.sum(df['sqr_err']))
        df.drop(['demand_sim', 'error', 'sqr_err'], axis=1)
        e += 0.01
    rd += 10

opt_error = np.min(sse)
e_optimal = x_axis[sse.index(opt_error)]
rd_optimal = y_axis[sse.index(opt_error)]

print('Optimal values of SSE = {}'.format(opt_error))
print('Optimal values of E that got optimal SSE = {}'.format(e_optimal))
print('Optimal values of RD that got optimal SSE = {}'.format(rd_optimal))


plt.contourf(np.array(sse).reshape(-1, 2))
plt.title('SSE optimal = ' + str(opt_error) + '\nE got optimal = ' + str(e_optimal) +
          '\nRD got optimal error = ' + str(rd_optimal))

plt.show()
