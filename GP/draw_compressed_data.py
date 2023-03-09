import pandas as pd
import plotly.graph_objects as go

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)


def draw_graph(data_frame, year_name):
    fig = go.Figure()
    products_list = sorted(list(data_frame['product_id'].unique()))

    for product_id in products_list:
        fig.add_trace(
            go.Scatter(
                x=data_frame['order_date'][data_frame['product_id'] == product_id],
                y=data_frame['quantities_sold'][data_frame['product_id'] == product_id],
                name=str(product_id), visible=True
            )
        )

    buttons = []

    for i, product_id in enumerate(products_list):
        args = [False] * len(products_list)
        args[i] = True

        button = dict(label=str(product_id),
                      method="update",
                      args=[{"visible": args}])

        buttons.append(button)

    fig.update_layout(
        updatemenus=[dict(
            active=0,
            type="dropdown",
            buttons=buttons,
            x=0,
            y=1.1,
            xanchor='left',
            yanchor='bottom'
        )],
        autosize=False,
        width=1000,
        height=800
    )

    fig.write_html('graphs\\year ' + year_name + ' products plot.html')


data_2019 = pd.read_excel('all years compressed data weekly.xlsx', sheet_name='2019')
data_2020 = pd.read_excel('all years compressed data weekly.xlsx', sheet_name='2020')
data_2021 = pd.read_excel('all years compressed data weekly.xlsx', sheet_name='2021')

draw_graph(data_2019, '2019')
draw_graph(data_2020, '2020')
draw_graph(data_2021, '2021')
