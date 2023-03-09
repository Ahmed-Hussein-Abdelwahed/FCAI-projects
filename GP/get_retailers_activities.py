import pandas as pd
import numpy as np

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


def get_retailer_less_than_ten_activities(data_frame, retailers_ids):
    retailer_less_than_ten_rows = list()

    for i in retailers_ids:
        temp_frame = data_frame[data_frame['retailer_id'] == i]

        if len(temp_frame) < 10:
            retailer_less_than_ten_rows.append(temp_frame)

    return retailer_less_than_ten_rows


def get_retailer_greater_than_ten_activities(data_frame, retailers_ids):
    retailer_greater_than_ten_rows = list()

    for i in retailers_ids:
        temp_frame = data_frame[data_frame['retailer_id'] == i]

        if len(temp_frame) > 10:
            retailer_greater_than_ten_rows.append(temp_frame)

    return retailer_greater_than_ten_rows


data_2019 = pd.read_excel('Data.xlsx', sheet_name='2019')
retailers_2019_ids = data_2019['retailer_id'].unique()

retailers_greater_ten = pd.concat(get_retailer_greater_than_ten_activities(data_2019, retailers_2019_ids))
retailers_less_ten = pd.concat(get_retailer_less_than_ten_activities(data_2019, retailers_2019_ids))

retailers_less_ten.to_excel('data files\\retailers less than 10 transactions.xlsx')
retailers_greater_ten.to_excel('data files\\retailers greater than 10 transactions.xlsx')
