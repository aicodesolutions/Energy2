import streamlit as st

#st.header("Your Estimated Consumption Today")
#st.write(f"You are logged in as {st.session_state.role}.")

import pandas as pd
df = pd.read_csv("EnergyHrs2.csv")  

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

#st.header("Your Estimated Generation Today")



if 1:
    st.write('Energy Dashboard')
    chart_data = df
    st.line_chart(chart_data)




#df = pd.read_csv("./data/titanic.csv")  

#df = pd.DataFrame({
#  #'Time': [1, 2, 3, 4,5,7,8,9,10,11,12,1,2],
#  'Actual kWh': [0.10, 0.20, 0.30, .40,.40,.40,.40,.20,.20,.20,.50,.50,.50],
#  'Estimated kWh': [0.00, 0.00, 0.10, .20,.30,.40,.40,.40,.30,.20,.40,.40,.40]
#})

df