""" Housing price prediction model using different features"""
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


"""  exploratory data analysis  """
df = pd.read_csv('USA_Housing.csv')
# print(df.columns)
# sns.heatmap(df.corr(), annot=True)
# plt.show()
# df.info()
print(df.columns)                                                                     ### from this we will grab the columns



"""  starting creatinf a model   """
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]        ### this data will be used as the features

y = df['Price']                                                   ### this data is the predicted outcome



""" we will have to split the data into training set and testing set with scikit learn  """
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.4, random_state=101)  ### tuple unpacking

lm = LinearRegression()                                                               ### this is the object
lm.fit(X_train, y_train)

print(lm.intercept_)                                                                  ### to evaluate the model
print(lm.coef_)                                                                       ### co-ef for each feature
cdf = pd.DataFrame(lm.coef_, X.columns, columns=['coeff'])
print(cdf)

"""  Predictions  """
predictions = pd.DataFrame(lm.predict(X_test))
print(predictions)
predictions.to_csv('predictions.csv')
plt.scatter(y_test, predictions)
sns.displot(y_test-predictions)
plt.show()


"""  Using and keeping metrices in mind """
from sklearn import metrics
print(metrics.mean_absolute_error(y_test, predictions))
print(metrics.mean_squared_error(y_test, predictions))
print(numpy.sqrt(metrics.mean_squared_error(y_test, predictions)))




