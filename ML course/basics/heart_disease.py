import pandas as pd
import matplotlib.pyplot as plt
# import cv2  # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread('6-step-ml-framework.png')
# # DISPLAY
# cv2.imshow('photo', img)
# cv2.waitKey(0)
# cv2.resize('photo', 20, 20)

pd.options.display.width = None
pd.options.display.max_rows = None
df = pd.read_csv('heart_disease.csv')

print(df.head(10))
plt.bar(df.target.value_counts(), height=1)
plt.show()
