import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import plotly.express as px

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs

# outlier_2019 = pd.read_excel('data files\\outliers 2019.xlsx')
# fig = px.scatter(outlier_2019, x='order_date', y='quantities_sold', color='product_id',
#                  hover_data=outlier_2019.columns, title='Year 2019 outliers')
# fig.write_html('data files\\Year 2019 outliers.html')

df = pd.read_excel('C:\\Users\\Lenovo\\Downloads\\test.xlsx', sheet_name='pid = 8 monthly')

df['order_date'] = pd.to_datetime(df['order_date'])
df['Time'] = np.arange(len(df.index))

print('Here =', df['Time'].corr(df['quantities_sold']))

# Training data
X = df.loc[:, ['Time']]  # features
y = df.loc[:, 'quantities_sold']  # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(X_test)

ddf = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(ddf)
print('=' * 80)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
