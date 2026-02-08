import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.text("Hello Mahmoud!")
btn = st.button("Submit")
if btn:
    st.info("Info")
option = st.radio("Select:", ("A", "B", "C"))
if option == "A":
    st.success("You selected A")
elif option == "B":
    st.warning("You selected B")
else:
    st.error("You selected C")
chk = st.checkbox("I agree to the terms and conditions")
if chk:
    st.success("Thank you for agreeing!")
box = st.selectbox("Choose a number:", ["A", "B", "C"])
if box=="A":
    st.warning("Warning!")
elif box=="B":
    st.error("Error!")
elif box=="C":
    st.success("Success!")
age = st.slider("Select your age:", 18, 100,18)
st.select_slider("Select:", ["A", "B", "C", "D", "E", "F"])
st.text_input("Enter your name:")
st.text_area("Enter your address:")
st.file_uploader("Upload a file:")
st.camera_input("Take a Photo")
st.date_input("Select a date:")
st.time_input("Select a time:")
st.number_input("Enter a number:")
st.multiselect("Select multiple options:", ["A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
st.color_picker("Pick a color:")
st.header("Data Frame")
df=sns.load_dataset("taxis")
#st.write(df)
st.subheader("Data Frame")
st.dataframe(df.head())  # interactive table
st.dataframe(df.sample(4))  # interactive table
btn=st.button("Show Data")
if btn:
    st.write(df.sample(10))
st.header("Table")
st.table(df.head())  # static table