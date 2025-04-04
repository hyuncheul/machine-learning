#KNN의 경우 차원이 높을수록 성능이 저하됨.

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
sns.set()
sns.pairplot(iris,hue='species',height=2.5)
#plt.show()
#print(iris.shape)
X= iris.drop('species',axis=1)
#print(X.shape)
y = iris['species']
from sklearn.preprocessing import LabelEncoder
import numpy as np
classle = LabelEncoder()
y=classle.fit_transform(iris['species'].values)
#print(np.unique(y))
yo = classle.inverse_transform(y)
#print('species:', np.unique(yo))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state =1, stratify = y)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5, p=2)
knn.fit(X_train_std,y_train)

y_test_pred = knn.predict(X_test_std)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_test_pred))