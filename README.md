# Forecasting Sales with Prophet (Django Web App)

# Project Objective
This project demonstrates a web application built using the Django framework that applies a time series forecasting model (Facebook Prophet) to retail sales data.
It allows users to input a forecast horizon (in weeks) and receive future sales predictions, along with visual plots and downloadable results.

# 📊 Dataset Description
The dataset used is weekly sales data from a retail store, containing:

Date: Week of sale

Store, Dept: Identifiers

Weekly_Sales: Target sales value

## 📊 Model
Model training and data preprocessing were performed in [this Colab notebook](https://colab.research.google.com/drive/151o-zjslCUb09JmHKCaYdeiU3b26imy5). It includes:

- 📂 Dataset loading and initial inspection
- 🧹 Handling missing and invalid dates
- 🏪 Filtering for Store 1, Department 1 to create a focused time series
- 📈 Prophet model training using weekly frequency
- 💾 Exporting the trained model as a `.pkl` file for integration with the Django web app


# ⚙️ Tech Stack
Django (Python Web Framework)

Prophet (Forecasting library by Meta)

Pandas & Matplotlib (Data handling and visualization)

Joblib (Model serialization)

HTML/CSS (Django Templates)

# 🧪 Features
📈 Forecasts future sales based on historical weekly data

📥 User inputs number of weeks to predict (horizon)

🖼️ Interactive forecast plot with uncertainty intervals

📎 Download forecast results as CSV

✅ Handles missing dates and invalid entries automatically

# 🔧 How to Run the App
1. Clone the Repository : https://github.com/InfasMohammed/Task-AI-Developer.git
2. Install Required Packages : Django
   prophet
   pandas
   matplotlib
   joblib
3. Run the Django Server : python manage.py runserver


# Output 

![image](https://github.com/user-attachments/assets/b69f1314-e74b-4798-b27d-ab089511fdb3)


