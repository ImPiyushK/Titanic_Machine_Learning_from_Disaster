# -*- coding: utf-8 -*-
"""Titanic(Piyush).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BU8m68QJOuODFdqM4gIk1eKTuBJyPCZa

##**TITANIC: MACHINE LEARNING FROM DISASTER**##

IMPORTING LIBRARIES
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import ensemble, model_selection

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

target = train["Survived"].values
features_forest = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values

forest = ensemble.RandomForestClassifier(
    max_depth = 7,
    min_samples_split = 4,
    n_estimators = 1000,
    random_state = 1,
    n_jobs = -1
)
forest = forest.fit(features_forest, target)

print(forest.feature_importances_)
print(forest.score(features_forest, target))

scores = model_selection.cross_val_score(forest, features_forest, target, scoring='accuracy', cv=10)
print (scores)
print (scores.mean())

test_features_forest = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
prediction_forest = forest.predict(test_features_forest)

PassengerId = np.array(test["PassengerId"]).astype(int)
solution = pd.DataFrame(prediction_forest, PassengerId, columns = ["Survived"])
solution.to_csv("random_forest.csv", index_label = ["PassengerId"])
print("Your submission was successfully saved!")
