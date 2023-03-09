import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.options.display.width = None
pd.options.display.max_rows = None

plt.plot()
plt.show()

plt.plot([1, 2, 3, 4])
plt.show()

x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y)
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
plt.show()

fig = plt.figure()  # does not work
ax = fig.add_axes([1, 1, 1, 1])
ax.plot(x, y)
plt.show()

# this is object oriented method that it is faster than API

fig, ax = plt.subplots()  # this method will be used in this course
ax.plot(x, y)
plt.show()

# Anatomy of a matplotlib figure

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x, y)
ax.set(title='simple plot',
       xlabel='x-axis',
       ylabel='y-axis')
fig.savefig('E:\\Python codes\\ML course\\sample-plot.png')  # directory to save the plot image

# scatter plot and bar plot

x = np.linspace(0, 10, 100)  # (start, stop, number of elements)create data to be plotted
fig, ax = plt.subplots()
ax.plot(x, x ** 2)

# make scatter plot

fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))

fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))

fig, ax = plt.subplots()
ax.scatter(x, np.cos(x))

fig, ax = plt.subplots()
ax.scatter(x, np.tan(x))
plt.show()

# and so on

# make bar chart

nut_butter_prices = {'Almond butter': 10,
                     'Peanut butter': 8,
                     'Cashew butter': 12}
fig, ax = plt.subplots()
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax.set(title='Dan\'s nut Butter Stores',
       ylabel='Price (s)')
plt.show()

# Histogram and subplots

fig, ax = plt.subplots()
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()))
# you can not use dictionary as passing values, so you must cast them into lists instead
plt.show()

fig, ax = plt.subplots()
ax.hist(np.random.randn(1000))  # (symmetric random numbers)
plt.show()

# subplots option 1

# you can show more than one figure in a single window as below
# below we have 4 figures ax1,ax2,ax3,ax4
# because we set nrows=2 and ncols=2
# you can set as you want

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2,
                                             ncols=2,
                                             figsize=(10, 5))
ax1.plot(x, x / 2)
ax2.scatter(np.random.random(10), np.random.random(10))
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(np.random.randn(10000))
plt.show()

# subplots option 2

fig, ax = plt.subplots(nrows=2,
                       ncols=2,
                       figsize=(10, 5))
# here is another method to access the figures using index as you see below [0, 0] means that arr[0][0]
ax[0, 0].plot(x, x / 2)
ax[0, 1].scatter(np.random.random(10), np.random.random(10))
ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1, 1].hist(np.random.randn(10000))
plt.show()

# plot range of dates cumsum() ==> cumulative summation
plt.plot(pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000)).cumsum())
plt.show()

# plotting from pandas dataframes

car_sales = pd.read_csv('car_sales.csv')
car_sales.plot(x='Make', y='Odometer (KM)', kind='barh')
plt.show()
car_sales['Odometer (KM)'].plot.hist()
plt.show()

car_sales['Price'] = car_sales['Price'].str.replace('[\$\,\.]', '')
car_sales['Price'] = car_sales['Price'].str[:-2]
car_sales['Sale Date'] = pd.date_range('1/1/2020', periods=len(car_sales))
car_sales['Total Sales'] = car_sales['Price'].astype(int).cumsum()
car_sales.to_csv('car_sales.csv')

car_sales.plot(x='Sale Date', y='Total Sales')
car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')

# here we label axes within passing you can do that if you pass data from dataframe

plt.show()
print(car_sales)

x = np.random.rand(10, 4)
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
df.plot(kind='bar')

heart_disease = pd.read_csv('heart_disease.csv')
heart_disease['age'].plot.hist(bins=30)
heart_disease.plot.hist(figsize=(10, 30), subplots=True)  # plot the whole dataframe
plt.show()

over_50 = heart_disease[heart_disease['age'] > 50]
fig, ax = plt.subplots(figsize=(10, 6))
over_50.plot(kind='scatter',
             x='age',
             y='chol',
             c='target',
             ax=ax)
ax.set_xlim([45, 100])
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(x=over_50['age'],
                     y=over_50['chol'],
                     c=over_50['target'])
ax.set(title='Heart Disease and cholesterol Level',
       xlabel='Age',
       ylabel='Cholesterol')
ax.legend(*scatter.legend_elements(), title='Target')
ax.axhline(over_50['chol'].mean(), linestyle='--')
plt.show()

fig, (ax0, ax1) = plt.subplots(nrows=2,
                               ncols=1,
                               figsize=(10, 10),
                               sharex=True)
scatter = ax0.scatter(x=over_50['age'],
                      y=over_50['chol'],
                      c=over_50['target'])
ax0.set(title='Heart Diseases and Cholesterol Levels',
        ylabel='Cholesterol')
ax0.legend(*scatter.legend_elements(), title='Target')
ax0.axhline(y=over_50['chol'].mean(),
            linestyle='--')
scatter = ax1.scatter(over_50['age'],
                      y=over_50['thalach'],
                      c=over_50['target'])
ax1.set(title='Heart Diseases and Max Heart Rate',
        xlabel='Age',
        ylabel='Max Heart Rate')
ax1.legend(*scatter.legend_elements(), title='Target')
ax1.axhline(y=over_50['thalach'].mean(),
            linestyle='--')
fig.suptitle('Heart Disease Analysis', fontsize=16, fontweight='bold')
plt.show()

# customizing your plots

print(plt.style.available)  # to show the available styles in plotting charts
plt.style.use('seaborn-whitegrid')  # to change the default style
plt.plot(car_sales['Price'])
car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')
plt.show()

plt.style.use('ggplot')
car_sales['Price'].plot()
plt.show()

# and so on

i = np.random.randn(10, 4)
dt = pd.DataFrame(i, columns=['a', 'b', 'c', 'd'])
ax = dt.plot(kind='bar')
ax.set(title='Random Number Bar Graph from DataFrame',
       xlabel='Row number',
       ylabel='Random number')
ax.legend().set_visible(True)
plt.show()

# if you want to customize the colors used in the graph you can use (cmap) within the ax block
