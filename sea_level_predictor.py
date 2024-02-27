import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    year = df["Year"]
    sea_level = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(year, sea_level, color='blue', label='Data Points')

    # Create first line of best fit
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

    # Extend line to the year 2050
    future_years = range(1880, 2051)
    future_line = slope * future_years + intercept
    plt.plot(future_years, future_line, linestyle='--', color='green', label='Prediction to 2050')

    # Create second line of best fit
    # Filter data from year 2000 to the most recent year
    recent_years_data = df[df["Year"] >= 2000]
    recent_year = recent_years_data["Year"]
    recent_sea_level = recent_years_data["CSIRO Adjusted Sea Level"]

    # Perform linear regression
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_year, recent_sea_level)

    # Extend line to the year 2050 starting from year 2000
    future_years_recent = range(2000, 2051)
    future_line_recent = slope_recent * future_years_recent + intercept_recent
    plt.plot(future_years_recent, future_line_recent, linestyle='--', color='purple', label='Prediction to 2050 (2000-present)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()