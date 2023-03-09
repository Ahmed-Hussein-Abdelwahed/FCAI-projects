import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


def get_products_data(data_frame, year1_ids, year2_ids, year3_ids):

    data_frame = data_frame.drop('retailer_id', axis=1)
    frames_list = list()
    for i in year1_ids:
        if i in year2_ids and i in year3_ids:
            frames_list.append(data_frame[data_frame['product_id'] == i].sort_values(by='order_date'))
    return frames_list

