import pandas as pd
import numpy as np

pd.options.display.width = None
pd.options.display.max_rows = None
pd.set_option('display.float_format', lambda x: '%.3f' % x)  # format numeric outputs


def drop_outliers(data_frame):
    data_frame.drop(data_frame['quantities_sold'].index[np.abs((data_frame['quantities_sold'] - data_frame['quantities_sold'].mean()) / data_frame['quantities_sold'].std()) > 3].tolist(), inplace=True)

