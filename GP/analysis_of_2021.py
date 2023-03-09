import pandas as pd
import plotly.express as px


pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


# outlier_2021 = pd.read_excel('data files\\outliers 2021.xlsx')
# fig = px.scatter(outlier_2021, x='order_date', y='quantities_sold', color='product_id',
#                  hover_data=outlier_2021.columns, title='Year 2021 outliers')
# fig.write_html('data files\\Year 2021 outliers.html')


