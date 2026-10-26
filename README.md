
# 🚗 Used Car Price Prediction

A Machine Learning project that predicts used car prices based on vehicle details using regression models and a Streamlit web application.

## 📌 Project Overview

Buying or selling a used car can be challenging because prices vary depending on several factors. This project uses regression models to estimate car prices from historical vehicle data.

The application is built with Python and Streamlit and provides a simple interface for entering vehicle details and viewing a predicted price.

## Features
- Predict estimated used car prices.
- Dynamic brand and model selection.
- Inputs for manufacturing year, kilometers driven, fuel type, and transmission.
- Interactive web interface built with Streamlit.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Streamlit
- Matplotlib and Seaborn
- Jupyter Notebook

## 🤖 Machine Learning Workflow

1. Load and inspect the dataset.
2. Perform data cleaning and exploratory data analysis.
3. Select input features and the target variable (`Price`).
4. Split the data into training and testing sets.
5. Encode categorical features using One-Hot Encoding.
6. Train and compare regression models:
   - Linear Regression
   - Random Forest Regressor
   - Gradient Boosting Regressor
7. Tune Gradient Boosting hyperparameters using GridSearchCV.
8. Evaluate the model using MAE, RMSE, and R².
9. Save the preprocessing and trained model in a pipeline.
10. Build a Streamlit application for price prediction.