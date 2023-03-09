import time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_rows = None


def close_event():
    plt.close()  # timer calls this function after 3 seconds and closes the window


df = pd.read_csv("New Microsoft Excel Worksheet.csv")

fig = plt.figure(figsize=(8, 5))
timer = fig.canvas.new_timer(interval=10000)  # creating a timer object and setting an interval of 10000 milliseconds
timer.add_callback(close_event)
flag = 'n'
while flag != 'y':
    try:
        product_id = int(input('Enter product id'))
        series = df[df['product_id'] == product_id]
        series.T  # Transpose the series
        plt.plot(series.T[1:])
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
        plt.xticks(rotation=90)
        timer.start()
        plt.show()
    except:
        print('product id is not found')
    finally:
        flag = input('exit (y or n)')
