"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  #'Time': [1, 2, 3, 4,5,7,8,9,10,11,12,1,2],
  'Actual kWh': [0.10, 0.20, 0.30, .40,.40,.40,.40,.20,.20,.20,.50,.50,.50],
  'Estimated kWh': [0.00, 0.00, 0.10, .20,.30,.40,.40,.40,.30,.20,.40,.40,.40]
})

df

import streamlit as st
import numpy as np
import pandas as pd

chart_data = df

st.line_chart(chart_data)



import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
""" 
# Running
python -m streamlit run your_script.py

# is equivalent to:
streamlit run dashboard.py 
"""