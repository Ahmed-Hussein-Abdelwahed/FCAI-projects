import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_rows = None

series = pd.Series(['BMW', 'Toyota', 'Honda'])
colors = pd.Series(['Red', 'Blue', 'White'])  # 1D array

# you can set indices for the elements as:

colors1 = pd.Series(['car', 'bus', 'bike', 'plane', 'scooter'], index=[2, 4, 5, 4, 10])
print(series)
print(colors)


# Dataframe ==> 2D (Rows and columns) [as dictionary]
# create dataframe from series

car_data = pd.DataFrame({'car make': series, 'colors': colors})
print(car_data)


# crate dataframe directly (import from csv file)

car_sales = pd.read_csv('car_sales.csv')

# create csv file contains the same data in car sales file its name is (exported_car_sales)

car_sales.to_csv('exported_car_sales.csv')
exported_car_sales = pd.read_csv('exported_car_sales.csv')
print(exported_car_sales)


# describe the dataframe


print(car_sales.dtypes)
print(car_sales.columns)
print(car_sales.index)
print(car_sales.describe())  # statistical description
print(car_sales.info())
print(pd.Series([10, 30, 100, 4, 150, 1879]).mean())
print(car_sales.mean())
print(car_sales.sum())
print(car_sales['Doors'].sum())
print(len(car_sales))  # number of rows


# select and viewing data with pandas

print(car_sales.head())  # top five rows by default to select number to be show pass number in ()
print(car_sales.tail())  # bottom five rows

# .loc ==> refers to index
# .iloc ==> refers to position

print(car_sales.loc[3])  # print the entire row
print(car_sales.iloc[3])  # same as .loc[3] [for this example only]

print(car_sales.Make, '\n\n')  # same [does not work if the column name contains a space]
print(car_sales['Make'])  # same

print(car_sales[car_sales['Make'] == 'Toyota'])  # condition on selection
print(car_sales[car_sales['Odometer (KM)'] > 100000])


print(pd.crosstab(car_sales['Make'], car_sales['Doors']), '\n\n')  # compare two columns

# to compare more than two columns

print(car_sales.groupby(['Make']).mean())

plt.plot(car_sales['Odometer (KM)'])
plt.hist(car_sales['Odometer (KM)'])

# if you have a column that its data type is object you can not plot that unless you convert into int as below

car_sales['Price'] = car_sales['Price'].str.replace('[\$\,\.]', '').astype(int)
plt.plot(car_sales['Price'])
plt.show()


# manipulating data

print(car_sales['Make'].str.lower())

# to check if the data have missing values or not (missing value will display as NaN)

car_sales_missing = pd.read_csv('car-sales-missing-data.csv')

# replace nan with mean value of Odometer

car_sales_missing['Odometer'].fillna(car_sales_missing['Odometer'].mean(), inplace=True)


# to remove nan from data

car_sales_missing.dropna(inplace=True)
print(car_sales_missing)


# to create new column in the dataframe
car_sales['Seats'] = pd.Series([5, 10, 10, 11, 12, 13, 14, 20, 25, 23])
car_sales['Fuel per 100KM'] = [12, 10, 8, 9, 4, 6.5, 13, 20, 5, 3]  # list length must be same as in dataframe

# crete column from another column

car_sales['Total fuel used (L)'] = car_sales['Odometer (KM)'] / 100 * car_sales['Fuel per 100KM']

# create a column from a single value

car_sales['Number of wheels'] = 4
car_sales['Passed road safety'] = True


# to drop column

car_sales = car_sales.drop('Total fuel used (L)', axis=1)

# this line is very important to save changes in the original file otherwise changes
# will show in console only then it will be crashed

car_sales.to_csv('car_sales.csv', index=False)


# to take a sample of your data you have sample function [machine learning training and testing]
# take random sample from your data (frac=num less tahn one ==> the percent you want to choose from the data)

print(car_sales.sample(frac=0.7))  # 70 %

car_sales['Odometer (KM)'] = car_sales['Odometer (KM)'].apply(lambda x: x/1.6)
car_sales.to_csv('car_sales.csv', index=False)
print(car_sales)
