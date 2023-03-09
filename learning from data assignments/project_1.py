import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.width = None
pd.options.display.max_rows = None

df = pd.read_csv('project_1_data_file.csv')

# training part

training_set = df.sample(frac=0.7)
test_set = df.sample(frac=0.3)

num_of_epochs = int((len(training_set.index)) / 1350)  # 50 epochs
epoch_size = 1350

wights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
b = 0.1
neta = 0.1

epoch_start = 0
epoch_end = 1350

epoch = training_set.iloc[epoch_start:epoch_end]

S = np.empty(epoch_size, float)
error = np.empty(epoch_size, float)
delta_wights = np.empty((epoch_size, 6), float)
delta_b = np.empty(epoch_size, float)
new_wights = np.empty((epoch_size, 6), float)
new_b = np.empty(epoch_size, float)
SE = np.empty(epoch_size, float)
MSE = np.empty(num_of_epochs, float)
results_df = pd.DataFrame(
    columns=['Output', 'Error', 'Delta_Wight_w1', 'Delta_Wight_w2', 'Delta_Wight_w3', 'Delta_Wight_w4', 'Delta_Wight_w5'
        , 'Delta_Wight_w6', 'Delta_b', 'Wights_w1', 'Wights_w2', 'Wights_w3', 'Wights_w4', 'Wights_w5', 'Wights_w6',
             'B', 'SE'])

for j in range(num_of_epochs):
    for i in range(epoch_size):
        S[i] = np.dot(epoch.iloc[i, 0:6], wights) + b
        error[i] = S[i] - epoch.iloc[i, 6]
        delta_wights[i, :] = np.dot(epoch.iloc[i, 0:6], error[i]) * neta
        delta_b[i] = neta * error[i]

        new_wights[i, :] = wights
        new_b[i] = b
        SE[i] = (error[i]) ** 2

        results_epoch = pd.DataFrame({'Output': S,
                                      'Error': error,
                                      'Delta_Wight_w1': delta_wights[:, 0],
                                      'Delta_Wight_w2': delta_wights[:, 1],
                                      'Delta_Wight_w3': delta_wights[:, 2],
                                      'Delta_Wight_w4': delta_wights[:, 3],
                                      'Delta_Wight_w5': delta_wights[:, 4],
                                      'Delta_Wight_w6': delta_wights[:, 5],
                                      'Delta_b': delta_b,
                                      'Wights_w1': new_wights[:, 0],
                                      'Wights_w2': new_wights[:, 1],
                                      'Wights_w3': new_wights[:, 2],
                                      'Wights_w4': new_wights[:, 3],
                                      'Wights_w5': new_wights[:, 4],
                                      'Wights_w6': new_wights[:, 5],
                                      'B': new_b,
                                      'SE': SE},
                                     index=epoch.index)
    results_df = results_df.append(results_epoch)

    wights = wights - np.mean(delta_wights)
    b = b - np.mean(delta_b)

    epoch_start += epoch_size
    epoch_end += epoch_size
    epoch = training_set.iloc[epoch_start:epoch_end]

    MSE[j] = np.mean(SE)

x = [i for i in range(1, 51)]

# testing part

num_of_epochs = int((len(test_set.index)) / 950)  # 30 epochs
epoch_size = 950

wights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
b = 0.1
neta = 0.1

epoch_start = 0
epoch_end = 950

epoch = test_set.iloc[epoch_start:epoch_end]

S1 = np.empty(epoch_size, float)
error1 = np.empty(epoch_size, float)
delta_wights1 = np.empty((epoch_size, 6), float)
delta_b1 = np.empty(epoch_size, float)
new_wights1 = np.empty((epoch_size, 6), float)
new_b1 = np.empty(epoch_size, float)
SE1 = np.empty(epoch_size, float)
MSE1 = np.empty(num_of_epochs, float)
results_df1 = pd.DataFrame(
    columns=['Output', 'Error', 'Delta_Wight_w1', 'Delta_Wight_w2', 'Delta_Wight_w3', 'Delta_Wight_w4', 'Delta_Wight_w5'
        , 'Delta_Wight_w6', 'Delta_b', 'Wights_w1', 'Wights_w2', 'Wights_w3', 'Wights_w4', 'Wights_w5', 'Wights_w6',
             'B', 'SE'])

for j in range(num_of_epochs):
    for i in range(epoch_size):
        S1[i] = np.dot(epoch.iloc[i, 0:6], wights) + b
        error1[i] = S1[i] - epoch.iloc[i, 6]
        delta_wights1[i, :] = np.dot(epoch.iloc[i, 0:6], error1[i]) * neta
        delta_b1[i] = neta * error1[i]

        new_wights1[i, :] = wights
        new_b1[i] = b
        SE1[i] = (error1[i]) ** 2

        results_epoch = pd.DataFrame({'Output': S1,
                                      'Error': error1,
                                      'Delta_Wight_w1': delta_wights1[:, 0],
                                      'Delta_Wight_w2': delta_wights1[:, 1],
                                      'Delta_Wight_w3': delta_wights1[:, 2],
                                      'Delta_Wight_w4': delta_wights1[:, 3],
                                      'Delta_Wight_w5': delta_wights1[:, 4],
                                      'Delta_Wight_w6': delta_wights1[:, 5],
                                      'Delta_b': delta_b1,
                                      'Wights_w1': new_wights1[:, 0],
                                      'Wights_w2': new_wights1[:, 1],
                                      'Wights_w3': new_wights1[:, 2],
                                      'Wights_w4': new_wights1[:, 3],
                                      'Wights_w5': new_wights1[:, 4],
                                      'Wights_w6': new_wights1[:, 5],
                                      'B': new_b1,
                                      'SE': SE1},
                                     index=epoch.index)
    results_df = results_df1.append(results_epoch)

    wights = wights - np.mean(delta_wights1)
    b = b - np.mean(delta_b1)

    epoch_start += epoch_size
    epoch_end += epoch_size
    epoch = test_set.iloc[epoch_start:epoch_end]

    MSE1[j] = np.mean(SE1)

x1 = [i for i in range(1, 31)]


fig, ((ax1), (ax2)) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax1.set(title='Error Calculation for training set',
        xlabel='Epoch Number',
        ylabel='MSE')
ax2.set(title='Error Calculation for testing set',
        xlabel='Epoch Number',
        ylabel='MSE')
ax1.plot(x, MSE)
ax2.plot(x1, MSE1)
plt.show()
