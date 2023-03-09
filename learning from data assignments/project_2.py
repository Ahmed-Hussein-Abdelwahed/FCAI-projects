import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from pandas_profiling import ProfileReport

pd.options.display.width = None
pd.options.display.max_rows = None

bank_data = pd.read_csv('project_2_data_file.csv')

# data Preprocessing

bank_data.drop_duplicates(subset=None, inplace=True)

# Notes:
# subset=None means that every column is used
# inplace=True  means that the data structure is changed and the duplicate rows are gone

bank_data.profile_report()
profile = ProfileReport(bank_data, title="Pandas Profiling Report")
profile.to_file("data_banknote_authentication.html")

x = bank_data.drop('class', axis=1)
y = bank_data['class']

# SVM model

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
hard_classifier = SVC(kernel='linear', C=100)  # hard margin
soft_classifier = SVC(kernel='linear')  # soft margin (C=1 [default value])

hard_classifier.fit(x_train, y_train)
soft_classifier.fit(x_train, y_train)
s_y_predicted = soft_classifier.predict(x_test)
h_y_predicted = hard_classifier.predict(x_test)

print('Soft margin SVM')
print(confusion_matrix(y_test, s_y_predicted))
print(classification_report(y_test, s_y_predicted))

print('\nHard margin SVM')
print(confusion_matrix(y_test, h_y_predicted))
print(classification_report(y_test, h_y_predicted))


fpr, tpr, thresholds = metrics.roc_curve(y_test, s_y_predicted)
# fpr ==> false positive rate
# tpr ==> true positive rate
# thresholds ==> for balancing the bias between nodes
roc_auc = metrics.auc(fpr, tpr)  # roc_auc ==> area under the curve
display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='Soft margin classifier')
display.plot()
plt.savefig('soft margin ROC curve.png')

fpr, tpr, thresholds = metrics.roc_curve(y_test, h_y_predicted)
roc_auc = metrics.auc(fpr, tpr)
display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='Hard margin classifier')

display.plot()
plt.savefig('hard margin Roc curve.png')
