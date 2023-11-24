# -*- coding: utf-8 -*-
"""Mini_project_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B1gRaLWAKzgKA2dslXaKEwUH85QMN9BK
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from torch.utils import tensorboard

# Load the data
iris_data = pd.read_csv('IRIS_Flower_Dataset.csv')

# Display basic information about the dataset and summary statistics
iris_data.info()
iris_data.describe()

# Visualize the data
sns.pairplot(iris_data, hue="species")
sns.pairplot(iris_data[['petal_width', 'petal_length', 'sepal_width', 'sepal_length']])
sns.jointplot(x=iris_data.sepal_length, y=iris_data.sepal_width)
sns.jointplot(x=iris_data.petal_length, y=iris_data.petal_width)
plt.show()

# Separate data into features and labels
y = iris_data['species']  # Labels
X = iris_data.drop('species', axis=1)  # Features

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Define hyperparameters for the SVM model
param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto'],
    'degree': [2, 3, 4],  # Add degrees for poly kernel
    'coef0': [0.0, 1.0, 2.0],  # Add values for coef0
    'shrinking': [True, False],
    'probability': [True, False],
    'class_weight': [None, 'balanced'],
    'tol': [1e-3, 1e-4, 1e-5],
}

# Initialize the SVM model
svm_model = SVC()

# Perform grid search with cross-validation to find the best hyperparameters
grid_search = GridSearchCV(estimator=svm_model, param_grid=param_grid, scoring='accuracy', cv=3)
grid_search.fit(X_train, y_train)

# Get the best hyperparameters
best_params = grid_search.best_params_
print(f"Best Hyperparameters: {best_params}")

# Train the model with the best hyperparameters
best_svm_model = SVC(**best_params)
best_svm_model.fit(X_train, y_train)

# Predict on the test set
predictions = best_svm_model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

# Classification report
print("Classification Report:")
print(classification_report(y_test, predictions))

# Save the SVM model
writer = tensorboard.SummaryWriter('models')
with open('models/svm_model.pkl', 'wb') as f:
    pickle.dump(svm_model, f)
print(svm_model)