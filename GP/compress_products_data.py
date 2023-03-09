import pandas as pd


pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


def compress_data_weekly(data_frame):

    frames_list = list()

    for i in data_frame['product_id'].unique():
        product_frame = data_frame[data_frame['product_id'] == i]
        temp_frame = product_frame.set_index('order_date').resample('W')['quantities_sold'].sum().reset_index()
        temp_frame.insert(1, 'product_id', i)

        frames_list.append(temp_frame.sort_values(by='order_date'))

    return frames_list


def compress_data_monthly(data_frame):

    frames_list = list()

    for i in data_frame['product_id'].unique():
        product_frame = data_frame[data_frame['product_id'] == i]
        temp_frame = product_frame.set_index('order_date').resample('M')['quantities_sold'].sum().reset_index()
        temp_frame.insert(1, 'product_id', i)

        frames_list.append(temp_frame.sort_values(by='order_date'))

    return frames_list


