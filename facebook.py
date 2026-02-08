import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px 
import plotly.graph_objects as go
import pickle
from sklearn.preprocessing import MinMaxScaler
st.set_page_config(page_title="Facebook Ads Analytics", page_icon=":bar_chart:", layout="wide")
# Load the dataset
df = pd.read_csv("facebook_ads.csv",encoding="ISO-8859-1")
# Display the dataset
st.title("Facebook Ads Analytics Dashboard📊")
option = st.sidebar.selectbox("Pick a  choice :",['Home','EDA','ML'])
# Home Page
if option == 'Home':
    st.title("Welcome to the Facebook Ads Analytics Dashboard!👋")
    st.markdown("## Author: **Mahmoud Mohamed**")
    st.write("This dashboard Visualizes user behaviour and predicts whether a user will click on a facebook ad.")
    st.dataframe(df.head())
# EDA Page
elif option == 'EDA':
    st.title("Exploratory Data Analysis (EDA)📈")
    st.markdown("Gain insights into how users interact with ads based on  **Time spent on site**,**Salary**, and whether They **Clicked**")
    #Layout
    col1, col2 = st.columns(2)
    #Scatter Plot
    st.subheader("Scatter Plot: Time Spent on Site vs Salary")
    fig = px.scatter(df, x="Time Spent on Site", y="Salary", trendline="ols", color="Clicked", title="Time Spent on Site vs Salary",color_discrete_sequence=["gray", "red"])
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### 🔍Insight:")
    st.info(
        "Users who **click ads** tend to spend **more time on the website**.\n\n"
         "Higher Salary does **not strongly influence** clicking behavior." )
    #Distribution Plot
    with col1:
        st.subheader("Distribution Plot: Time Spent on Site")
        fig = px.histogram(df, x="Time Spent on Site", nbins=25 , color="Clicked", marginal="box" , title="Distribution of Time Spent on Site")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 🔍Insight:")
        st.info("" \
        "The Majority spend **lower to mid-range** time on the site.\n\n"
        "Users who spend **very high time** are more likely to click on ads.")

    with col2:
        st.subheader("Clicked vs Not Clicked")
        fig = px.pie(df, names="Clicked", title="Clicked vs Not Clicked", color_discrete_sequence=["skyblue", "red"] , hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("### 🔍Insight:")
        st.info("The pie chart shows that a **small percentage** of users click on ads, while the majority do not.")

        #Salary Distribution
        st.subheader("Salary Distribution by Clicked status")
        fig = px.violin(df, x="Clicked", y="Salary", box=True , color="Clicked", title="Salary Distribution by Clicked status")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("### 🔍Insight:")
        st.info(
        "Salary does **not significantly differ** between users who click and those who do not.\n\n"
        "Ad behaviour seems  driven more by **time spent on site** than by salary.")
        
# ML Page
elif option == 'ML':
    st.title("🤖Ads Clicks Prediction model")
    st.write("Enter the user inputs below to predict whether a user will click on a Facebook ad or not.")
    # User Inputs
    time = st.number_input("Time Spent on Site (in minutes)")
    salary = st.number_input("Salary (in dollars)")
    
    btn = st.button("Predict")
    
    ms = MinMaxScaler()
    clf = pickle.load(open("my_model.pkl","rb"))
    result = clf.predict(([[time, salary]]))

    if btn:
        if result == 1:
            st.success("The user is likely to click on the ad.")
        else:
            st.warning("The user is unlikely to click on the ad.")