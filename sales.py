import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Sale Dashboard")
st.write("This app will display based on region and time")

data = {
  'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
  'Region': ['North', 'South', 'East', 'West', 'Central']
  'Sales Amount': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
}
df = pd.DataFrame(data)

year = st.slider("Choose a year", min_value = 2010, max_value = 2020, value = 2015)

st.write(f"Data for the year {selected_year}:")
filtered_df = df[df['Year'] == selected_year]
st.write(filtered_df)

fig, ax =plt.subplots()
ax.bar(filtered_df['Region'], filtered_df['Sales Amount'], colors='skyblue'}
plt.title(f'Sales in {selected_year}')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
st.pyplot(fig)
