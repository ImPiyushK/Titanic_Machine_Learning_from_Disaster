# Titanic Machine Learning from Disaster

This repository contains a machine learning project for predicting survival of passengers who travelled on Titanic Ship in 1912.

![Display Image](RawData/image1.jpg)

## Problem Description
This project highlights my approach to the introductory machine learning competition on Kaggle website- [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic).

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

This project analyses which people were likely to survive. In particular, tools of machine learning have been used to predict which passengers survived the tragedy.

## File Description

* Titanic.ipynb - Jupyter Notebook which contains python code for predicting survival.<br>
* titanic.py - Python code for predicting model.<br>
* Output - contains output files generated from different algorithm.<br>
* Dataset- contains training and testing data.<br>
  * test.csv - Testing Data
  * train.csv - Training Data
  * gender_submission.csv - Sample submission file
* readme.md - for guide to this project.<br>

## Project Description
This project has been made in Google Colab. 
The project uses a 5 step process for it's predicting task which is as follows:
1. Perform statistical analysis of data to find whether any of the entries is missing or not.
2. After performing statistical analysis, do a visual analysis by plotting the data using different bar graphs.
3. Used Feature Engineering technique to fill empty data(Fare, Age) with median of columns and changed sex column to 0,1 where male=0, female=1 and finally changed Embarked column to 0,1,2 where S=0, C=1, Q=2
4. Implemented multiple machine learning algorithm like Random Forest, Logistic Regression, Naive Bayues, SVM, KNN and Decision Tree to find which one is better for prediction.
5. Predicting and calculating the accuracy using Cross Validation Accuracy.

## Algorithm Performance
The procedure mentioned above in Project Description was successful in yielding decent results. The procedure gives cross validation accuracy of 0.828 with random forest. Other algorithms give the following results:
Logistic Regression: 0.795
Naive Bayes: 0.786
SVM: 0.786
KNN: 0.704
Decision Tree: 0.787
