import pandas as pd
import numpy as np
import plotly.express as px

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs

df = pd.read_excel("C:\\Users\\Lenovo\Downloads\\test.xlsx", sheet_name='pid = 8 daily')

temp_df = df['quantities_sold']
# l = list()
#
# q1 = df['quantities_sold'].quantile(0.25)
# q3 = df['quantities_sold'].quantile(0.75)
# iqr = q3 - q1
#
# for i in df['quantities_sold']:
#     if i < (q1 - 1.5 * iqr) or i > (q3 + 1.5 * iqr):
#         l.append(i)
#
# print('daily')
# print(len(l), ' out of ', len(df))
# print(l)
# print('*' * 100)


# df = pd.read_excel("C:\\Users\\Lenovo\Downloads\\test.xlsx", sheet_name='pid = 8 weekly')
#
# l = list()
#
# q1 = df['quantities_sold'].quantile(0.25)
# q3 = df['quantities_sold'].quantile(0.75)
# iqr = q3 - q1
#
# for i in df['quantities_sold']:
#     if i < (q1 - 1.5 * iqr) or i > (q3 + 1.5 * iqr):
#         l.append(i)
#
# print('weekly')
# print(len(l), ' out of ', len(df))
# print(l)
# print('*' * 100)
#
# df = pd.read_excel("C:\\Users\\Lenovo\Downloads\\test.xlsx", sheet_name='pid = 8 monthly')
#
# l = list()
#
# q1 = df['quantities_sold'].quantile(0.25)
# q3 = df['quantities_sold'].quantile(0.75)
# iqr = q3 - q1
#
# for i in df['quantities_sold']:
#     if i < (q1 - 1.5 * iqr) or i > (q3 + 1.5 * iqr):
#         l.append(i)
#
# print('monthly')
# print(len(l), ' out of ', len(df))
# print(l)

# outlier_2020 = pd.read_excel('data files\\outliers 2020.xlsx')
# fig = px.scatter(outlier_2020, x='order_date', y='quantities_sold', color='product_id',
#                  hover_data=outlier_2020.columns, title='Year 2020 outliers')
# fig.write_html('data files\\Year 2020 outliers.html')
