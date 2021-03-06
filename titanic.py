# -*- coding: utf-8 -*-
"""Titanic(Piyush).ipynb

##**TITANIC: MACHINE LEARNING FROM DISASTER**##

IMPORTING LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""READING TRANING AND TESTING DATA FROM CSV FILE"""

train = pd.read_csv("/content/drive/My Drive/Titanic dataset/train.csv")
train.head()

test = pd.read_csv("/content/drive/My Drive/Titanic dataset/test.csv")
test.head()

"""EXPLORATORY DATA ANALYSIS"""

plt.subplot2grid((2,3), (0,0))
train.Survived.value_counts(normalize=True).plot(kind="bar")
plt.title("Survived")

plt.subplot2grid((2,3), (0,1))
plt.scatter(train.Survived, train.Age, alpha=0.1)
plt.title("Age Survived")

plt.subplot2grid((2,3), (0,2))
train.Pclass.value_counts(normalize=True).plot(kind="bar")
plt.title("Class")

plt.subplot2grid((2,3),(1,0), colspan=2)
for x in [1,2,3]:
    train.Age[train.Pclass == x].plot(kind="kde")
plt.xlabel("Age")
plt.title("Age Distribution within Classes")
plt.legend(("1st Class", "2nd Class", "3rd Class"))

plt.subplot2grid((2,3),(1,2))
train.Embarked.value_counts(normalize=True).plot(kind='bar', alpha=0.55)
plt.title("Passengers boarding location")

print(train.shape)

"""FEATURE ENGINEERING"""

def clean_data(data):
    data["Fare"] = data["Fare"].fillna(data["Fare"].dropna().median())
    data["Age"] = data["Age"].fillna(data["Age"].dropna().median())

    data.loc[data["Sex"] == "male", "Sex"] = 0
    data.loc[data["Sex"] == "female", "Sex"] = 1

    data["Embarked"] = data["Embarked"].fillna("S")
    data.loc[data["Embarked"] == "S", "Embarked"] = 0
    data.loc[data["Embarked"] == "C", "Embarked"] = 1
    data.loc[data["Embarked"] == "Q", "Embarked"] = 2

clean_data(train)
clean_data(test)

"""MODELLING"""

from sklearn.model_selection import cross_val_score
target = train["Survived"].values
features_forest = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
test_features_forest = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

"""RANDOM FOREST"""

from sklearn.ensemble import RandomForestClassifier
forest = ensemble.RandomForestClassifier(
    max_depth = 7,
    min_samples_split = 4,
    n_estimators = 1000,
    random_state = 1,
    n_jobs = -1
)
forest = forest.fit(features_forest, target)

prediction_forest = forest.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(prediction_forest, PassengerId, columns = ["Survived"])
solution.to_csv("random_forest.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores = model_selection.cross_val_score(forest, features_forest, target, scoring='accuracy', cv=10)
print (scores.mean())

"""LOGISTIC REGRESSION"""

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(max_iter = 1000)
log_reg = log_reg.fit(features_forest, target)

log_pred=log_reg.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(log_pred, PassengerId, columns = ["Survived"])
solution.to_csv("logistic regression.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores_log = cross_val_score(log_reg, features_forest, target, scoring='accuracy', cv=10)
print('Cross-Validation Accuracy Score',scores_log.mean())

"""NAIVE BAIYES"""

from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(features_forest, target) 

gnb_pred = gnb.predict(test_features_forest) 

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(gnb_pred, PassengerId, columns = ["Survived"])
solution.to_csv("naive_bayes.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores_log = cross_val_score(gnb, features_forest, target, scoring='accuracy', cv=10)
print('Cross-Validation Accuracy Score',scores_log.mean())

"""SVM"""

from sklearn import svm
sv=svm.SVC(kernel='linear')
sv.fit(features_forest, target)

sv_pred=sv.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(sv_pred, PassengerId, columns = ["Survived"])
solution.to_csv("svm.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores_log = cross_val_score(sv, features_forest, target, scoring='accuracy', cv=10)
print('Cross-Validation Accuracy Score',scores_log.mean())

"""KNN"""

from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors=7) 
knn.fit(features_forest, target)

knn_pred=knn.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(knn_pred, PassengerId, columns = ["Survived"])
solution.to_csv("knn.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores_log = cross_val_score(knn, features_forest, target, scoring='accuracy', cv=10)
print('Cross-Validation Accuracy Score',scores_log.mean())

"""DECISION TREE"""

from sklearn.tree import DecisionTreeClassifier
dst=DecisionTreeClassifier()
dst.fit(features_forest, target)

dst_pred=dst.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(dst_pred, PassengerId, columns = ["Survived"])
solution.to_csv("decision_tree.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")

scores_log = cross_val_score(dst, features_forest, target, scoring='accuracy', cv=10)
print('Cross-Validation Accuracy Score',scores_log.mean())

