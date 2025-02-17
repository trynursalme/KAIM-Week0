import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from utils import load_data, calculate_z_scores

#load data fro the application
data = load_data('C:/Users/NurselamHussen-ZOAEt/Downloads/New folder/10 Academy-project/Week-0/KAIM-Week0/notebooks/merged_data_new.csv')

# Sidebar for user inputs
st.sidebar.title("Solar Radiation Dashboard")
country = st.sidebar.selectbox("Select Country", data['Country'].unique())
variable = st.sidebar.selectbox("Select Variable", ['GHI', 'DNI', 'DHI', 'Tamb', 'WS'])

# Filter data based on selected country
filtered_data = data[data['Country'] == country]

# Title and description
st.title("Solar Radiation Analysis Dashboard")
st.write(f"Exploring solar radiation and environmental data for **{country}**.")

# Line chart for time series analysis
st.subheader(f"{variable} Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data.index, filtered_data[variable], label=variable, color='blue')
ax.set_title(f"{variable} Over Time")
ax.set_xlabel("Date")
ax.set_ylabel(variable)
st.pyplot(fig)

# Histogram for variable distribution
st.subheader(f"Histogram of {variable}")
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(filtered_data[variable], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax.set_title(f"Distribution of {variable}")
ax.set_xlabel(variable)
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Interactive scatter plot
st.subheader("Scatter Plot: GHI vs Tamb")
ws_range = st.slider("Select Wind Speed Range (m/s)", float(filtered_data['WS'].min()), float(filtered_data['WS'].max()), (0.0, 5.0))
filtered_scatter = filtered_data[(filtered_data['WS'] >= ws_range[0]) & (filtered_data['WS'] <= ws_range[1])]
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=filtered_scatter['GHI'], y=filtered_scatter['Tamb'], hue=filtered_scatter['WS'], palette='viridis', ax=ax)
ax.set_title("GHI vs Tamb (Colored by WS)")
ax.set_xlabel("GHI (W/m²)")
ax.set_ylabel("Tamb (°C)")
st.pyplot(fig)

# Polar plot for wind analysis
st.subheader("Wind Speed and Direction Distribution")
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
ax.scatter(np.deg2rad(filtered_data['WD']), filtered_data['WS'], c=filtered_data['WS'], cmap='viridis', alpha=0.7)
ax.set_theta_zero_location('N')  # Set 0° (North) at the top
ax.set_theta_direction(-1)       # Clockwise direction
ax.set_title("Wind Speed and Direction Distribution", va='bottom')
st.pyplot(fig)

# Z-score analysis
st.subheader("Outliers Detection Using Z-Scores")
z_scores = calculate_z_scores(filtered_data, ['GHI', 'DNI', 'DHI', 'WS'])
outliers = filtered_data[(abs(z_scores['GHI']) > 3) | (abs(z_scores['DNI']) > 3)]
st.write("Outliers:")
st.dataframe(outliers.head())

# Footer
st.markdown("---")
st.write("Developed with ❤️ by Nurselam using Streamlit.")