📊 Facebook Ads Prediction System

An end-to-end machine learning project that predicts whether a user is likely to click on a Facebook advertisement based on their behavior and demographic features. The trained model is deployed using Streamlit, providing an interactive web interface for real-time predictions.

🚀 Project Overview

This project follows a proper machine learning workflow:

Load and preprocess Facebook ads data

Train a supervised ML model

Evaluate model performance

Save the trained model and scaler

Deploy the model using Streamlit for inference

The goal is to help understand user behavior and improve ad targeting decisions.

🧠 Machine Learning Details

Problem Type: Binary Classification

Target Variable: Clicked on Ad (Yes / No)

Features Used:

Time Spent on Site

Salary

Model Used: Logistic Regression

Preprocessing: MinMax Scaling

🛠️ Tech Stack

Python

pandas

NumPy

scikit-learn

Streamlit

Pickle

📁 Project Structure
Stream/
│

├── facebook.py          # Streamlit application

├── train_model.py       # Model training script

├── facebook_ads.csv     # Dataset

├── my_model.pkl         # Trained model

├── scaler.pkl           # Saved scaler

└── README.md

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/facebook-ads-prediction.git
cd facebook-ads-prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Train the model (run once)
python train_model.py


This will generate:

my_model.pkl

scaler.pkl

4️⃣ Run the Streamlit app
streamlit run facebook.py


Then open:

http://localhost:8501

🖥️ Application Output

The Streamlit app allows users to:

Enter time spent on site

Enter salary

Get a prediction indicating whether the user is likely or unlikely to click on the ad

📈 Model Evaluation

Model performance is evaluated during training using accuracy and standard classification metrics. The trained model and preprocessing steps are saved for consistent inference during deployment.

📌 Key Learnings

Proper separation between training and inference

Importance of saving preprocessing steps

Deploying ML models using Streamlit

Building reproducible ML pipelines

🔮 Future Improvements

Add more features to improve accuracy

Try advanced models (Random Forest, XGBoost)

Add model explainability (SHAP)

Deploy the app online

👤 Author

Mahmoud Noby
Aspiring Data Analyst / Machine Learning Enthusiast
