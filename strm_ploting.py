import streamlit as st
import pandas as pd
import numpy as np

st.title('Plotting using streamlit')
data=pd.DataFrame(np.random.randn(100,3), columns=['A','B','C'])
# st.write(data)
# st.table(data)
st.line_chart(data)