import streamlit as st
import numpy as np
import pandas as pd

st.title('Model Monitoring Dashboard')
data = pd.DataFrame({
    'Metric': ['Latency', 'Accuracy', 'Uptime'],
    'Value': [120, 0.94, 99.9]
})
st.table(data)