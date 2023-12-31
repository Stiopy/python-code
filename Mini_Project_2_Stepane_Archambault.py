# -*- coding: utf-8 -*-
"""Mini_project_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ORpbaVN_7ZSUMOXQqKUMU-QpBd1IX4lm
"""

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
data = pd.read_excel('Telco_customer_churn.xlsx')

# Display basic information about the dataset and summary statistics
data.info()
data.describe()

# Visualize the distribution of the target variable
sns.countplot(x='Churn Label', data=data)
plt.show()

# Drop irrelevant columns
data = data.drop(['CustomerID', 'Count', 'Churn Score', 'CLTV', 'Churn Reason', 'Country', 'State', 'Internet Service', 'Churn Label', 'Lat Long'], axis=1)

# One-hot encode categorical columns to convert them into numerical features
data = pd.get_dummies(data, columns=['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Phone Service', 'Multiple Lines',
                                     'Online Security', 'Online Backup', 'Device Protection', 'Tech Support',
                                     'Streaming TV', 'Streaming Movies', 'Contract', 'Paperless Billing', 'Payment Method', 'City'],
                      drop_first=True)

# Separate data into features and labels
y = data['Churn Value']  # Labels
X = data.drop('Churn Value', axis=1)  # Features

# Identify columns containing empty strings
columns_with_empty_strings = X.columns[X.applymap(lambda x: isinstance(x, str) and x.isspace()).any()]

# Display rows containing empty strings in these columns
rows_with_empty_strings = X[X[columns_with_empty_strings].apply(lambda x: x.str.isspace()).any(axis=1)]
#print(rows_with_empty_strings)

# Replace empty strings with the mean of values in each column
X[columns_with_empty_strings] = X[columns_with_empty_strings].apply(lambda x: pd.to_numeric(x, errors='coerce'))
X = X.fillna(X.mean())

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the hyperparameters to test
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'bootstrap': [True, False],
    'criterion': ['gini', 'entropy']
}

# Define the hyperparameters to test
'''
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False],
    'criterion': ['gini', 'entropy'],
    'max_features': ['sqrt', 'log2', None],
    'class_weight': [None, 'balanced'],
    'max_samples': [None, 0.5, 0.7, 0.9],
    'warm_start': [True, False],
    'oob_score': [True, False]
}
'''

# Initialize the Random Forest model
rf_model = RandomForestClassifier()

# Perform grid search with cross-validation to find the best hyperparameters
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, scoring='accuracy', cv=3)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_
print(f"Best Hyperparameters: {best_params}")

# Train the model with the best hyperparameters
best_rf_model = RandomForestClassifier(**best_params)
best_rf_model.fit(X_train, y_train)

# Predictions on the test set
y_pred = best_rf_model.predict(X_test)

# Save the best RF model
joblib.dump(best_rf_model, 'best_random_forest_model.pkl')

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))