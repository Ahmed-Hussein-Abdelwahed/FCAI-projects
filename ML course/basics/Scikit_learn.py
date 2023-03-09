# our problem is classification
# we want to specify is there or not


# 0. An end-to-end Scikit-learn workflow
# 1. Get the data ready
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split  # split data into train and test split
from sklearn.ensemble import RandomForestClassifier  # classification machine learning model


pd.options.display.width = None
pd.options.display.max_rows = None

heart_disease = pd.read_csv('heart_disease.csv')

# create x (feature matrix)

x = heart_disease.drop('target', axis=1)

# create y (labels)

y = heart_disease['target']

# 2.choose the right estimator/algorithm and hyper parameters  for our problem

clf = RandomForestClassifier(n_estimators=100)  # classify scikit learn

# we 'll keep the default hyper parameters

# print(clf.get_params())

# 3.fit the model/algorithm and use it to make prediction on our data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)  # test size = % 20 of data
clf.fit(x_train, y_train)  # to find patterns in the training data

# make a prediction

y_preds = clf.predict(x_test)

# 4. Evaluating model on the training data and testing data

# print(clf.score(x_train, y_train))
# output: 1.0 means that the model has done 100 percent one point zero
# print(clf.score(x_test, y_test))


# print(classification_report(y_test, y_preds))
# print(confusion_matrix(y_test, y_preds))
# print(accuracy_score(y_test, y_preds))

# 5. Improve a model
# try different amount of n_estimators
np.random.seed(42)

for i in range(10, 100, 10):
    print(f'Trying model with {i} estimators...')
    clf = RandomForestClassifier(n_estimators=i).fit(x_train, y_train)
    print(f'Model accuracy on test set: {clf.score(x_test, y_test) * 100:.2f} % ')
    print('')

# 6. Save and load a trained model

pickle.dump(clf, open('random_forest_model_1.pkl', 'wb'))
loaded_model = pickle.load(open('random_forest_model_1.pkl', 'rb'))
print(loaded_model.score(x_test, y_test))

# 7. Putting it all together

