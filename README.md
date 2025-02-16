# Solar Radiation Data Analysis Project

### Overview
#### The goal of this project is to analyze solar radiation measurement data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar installations. The analysis includes exploratory data analysis (EDA), statistical thinking, visualization, and dashboard development using Streamlit.

## Business Objective
#### The objective of this project is to support MoonLight Energy Solutions in developing a strategic approach to enhance operational efficiency and sustainability through targeted solar investments. As an Analytics Engineer, the task is to:

#### Perform exploratory data analysis (EDA) on environmental measurement data.
#### Translate insights into actionable recommendations for identifying high-potential regions for solar installations.
#### Build a Streamlit dashboard to visualize key findings and trends.
***
## Dataset Overview
#### The dataset used in this project is extracted and aggregated from Solar Radiation Measurement Data . Each row contains the following variables:

#### * Timestamp : Date and time of each observation.
#### * GHI (W/m²) : Global Horizontal Irradiance.
#### * DNI (W/m²) : Direct Normal Irradiance.
#### * DHI (W/m²) : Diffuse Horizontal Irradiance.
#### * ModA & ModB (W/m²) : Sensor measurements.
#### * Tamb (°C) : Ambient Temperature.
#### * RH(%) : Relative Humidity.
#### * WS (m/s) : Wind Speed.
#### * WSgust (m/s) : Maximum Wind Gust Speed.
#### * WD (°N to east) : Wind Direction.
#### * BP (hPa) : Barometric Pressure.
#### * Cleaning (1 or 0) : Indicates whether cleaning events occurred.
#### * Precipitation (mm/min) : Precipitation rate.
#### * TModA & TModB (°C) : Module temperatures.
#### * Country : Region (Benin, Sierra Leone, Togo).


## Dashboard Development
#### * Design and developed a Streamlit dashboard to visualize key insight.
#### * Integrated interactive features such as sliders, dropdowns, and buttons.
#### * Deployed the dashboard to streamlit Community Cloud.

*** 

## Key Features of the dashboard.
#### The streamlit dashboard includes the following interactive visualizations: 

#### * ***Line Charts :*** Time Series analysis of GHI, DNI, DHI, and Tamb.
#### * ***Histogram :*** Frequency distributions of key variables.
#### * ***Polar plots :*** Wind speed and direction distribution.
#### * ***Scatter Plots :*** Relationships between variables like GHI vs. Tamb
#### * ***Outlier Detection :*** Highlighting anomalies using Z-scores.

***

# How to Run the Project
## Prerequisites
#### * Python 3.x installed
#### * Required Libraries installed via requirements.txt

## Steps

#### Clone the repository
git clone https://github.com/trynursalme/KAIM-Week0.git
cd KAIM-Weeko
#### Install dependencies
pip install -r requirements.txt
#### Run the Streamlit app 
streamlit run app/main.py

## Future Improvements
#### * Incorporate machine learning models to predict solar irradiance.
#### * Add more advanced statistical analyses (e.g., hypothesis testing).
#### * Enhance the dashboard with additional interactivity and visualizations.

## Acknowledgments
#### Special thanks to the entire 10 Academy team for their guidance and support throughout this challenge.

## Contributing
#### If you’d like to contribute to this project, feel free to fork the repository and submit pull requests. 
#### For major changes, please open an issue first to discuss what you’d like to add or modify.