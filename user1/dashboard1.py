import streamlit as st


import pandas as pd
df = pd.read_csv("EnergyHrs1.csv")  

df = df.set_index("Datetime")
df.index = pd.to_datetime(df.index)
#
if 0:
    df['date'] = df.index
 
    df['hour'] = df['date'].dt.hour
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df['year'] = df['date'].dt.year
    
#
if 0:
    # Define app inputs
    inputs = {
        'hour': st.slider("Select Time (hour)", min_value=0, max_value=23),
        'day': st.slider("Select date", min_value=1, max_value=31),
        'month': st.slider('Select Month', min_value=1, max_value=12),
        'year': st.slider('Select Year', min_value=2004, max_value=2023)
    }

    # Preprocess input and make prediction
    df = pd.DataFrame(inputs, index=[0])

#
if 1:
    st.write('Energy Dashboard')
    chart_data = df
    st.line_chart(chart_data)

import streamlit as st
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Solar', 'Fossil','Wind', 'BioFuel'
sizes = [45, 15, 30, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

df