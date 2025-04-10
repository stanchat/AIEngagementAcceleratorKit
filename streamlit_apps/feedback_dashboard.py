import streamlit as st
import pandas as pd

st.title('Stakeholder Feedback Dashboard')
uploaded_file = st.file_uploader('Upload Feedback CSV')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.bar_chart(df['Satisfaction Score'])