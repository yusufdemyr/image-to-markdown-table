import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

dataset = pd.read_csv('my_file.csv')

# The recommended approach of using Label Encoding converts to integers which the DecisionTreeClassifier() will treat as numeric
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

dataset['Body Temperature'] =  labelencoder.fit_transform(dataset['Body Temperature'].values)
dataset['Gives Birth'] =  labelencoder.fit_transform(dataset['Gives Birth'].values)
dataset['Four-legged'] =  labelencoder.fit_transform(dataset['Four-legged'].values)
dataset['Hipernates'] =  labelencoder.fit_transform(dataset['Hipernates'].values)
dataset['Class'] = labelencoder.fit_transform(dataset['Class'].values)



X = dataset.drop('Class',axis=1)
y = dataset.loc[:,'Class']

X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.3)

decisionTree = DecisionTreeClassifier()

decisionTree.fit(X_train,y_train)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,5))
plot_tree(decisionTree,
          max_depth=10,
          feature_names=X.columns)
plt.show()

decisionTree_pred = decisionTree.predict(X_test)
print(classification_report(y_test,decisionTree_pred))