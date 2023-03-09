import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


def get_retailer_transactions(data_frame, retailers_id):
    frames = list()
    for i in retailers_id:
        temp_frame = data_frame[data_frame['retailer_id'] == i]
        products_ids = temp_frame['product_id'].unique()

        for j in products_ids:
            temp_frame1 = temp_frame[temp_frame['product_id'] == j]

            if len(temp_frame1) >= 10:
                frames.append(temp_frame1)
    return frames


def get_retailer_30_transactions(data_frame, retailers_id):
    frames = list()
    for i in retailers_id:
        temp_frame = data_frame[data_frame['retailer_id'] == i]

        if len(temp_frame) >= 30:
            frames.append(temp_frame)
    return frames

# data_2021 = pd.concat(pd.read_excel('all years retailers have 30 transactions or more.xlsx',
#                                     sheet_name=['2021 - 1', '2021 - 2', '2021 - 3']), ignore_index=True)
#
# retailers = data_2021['retailer_id'].unique()
#
# df = get_retailer_transactions(data_2021, retailers)
#
#
# pd.concat(df[0:int(len(df)/2)]).to_excel('get_products_1.xlsx', sheet_name='2021 - 1')
# pd.concat(df[int(len(df)/2):]).to_excel('get_products_2.xlsx', sheet_name='2021 - 2')


# data_2021 = pd.concat(pd.read_excel('data files\\Data.xlsx', sheet_name=['2021 - 1', '2021 - 2', '2021 - 3']),
#                       ignore_index=True)
# retailers_ids = data_2021['retailer_id'].unique()
#
# df = get_retailer_30_transactions(data_2021, retailers_ids)
#
# pd.concat(df[0:1000]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_1.xlsx', sheet_name='2021 - 1')
#
# pd.concat(df[1000:3000]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_2.xlsx', sheet_name='2021 - 2')
#
# pd.concat(df[3000:5000]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_3.xlsx', sheet_name='2021 - 3')
#
# pd.concat(df[5000:7000]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_4.xlsx', sheet_name='2021 - 4')
#
# pd.concat(df[7000:9000]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_5.xlsx', sheet_name='2021 - 5')
#
# pd.concat(df[9000:]).to_excel(
#     '2021 retailers have greater than 30 transactions or more_6.xlsx', sheet_name='2021 - 6')
#
