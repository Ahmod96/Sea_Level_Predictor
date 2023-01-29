import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (14,8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    results = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = results.slope
    intercept = results.intercept
    new_x_axis = pd.concat([df['Year'], pd.Series(list(range(2014, 2051)))])
    new_y_axis = slope*new_x_axis + intercept
    ax.plot(new_x_axis, new_y_axis)

    # Create second line of best fit
    results1 = linregress(df['Year'][120:], df['CSIRO Adjusted Sea Level'][120:])
    slope1 = results1.slope
    intercept1 = results1.intercept
    new_x1_axis = pd.concat([df['Year'][120:], pd.Series(list(range(2014, 2051)))])
    new_y1_axis = slope1*new_x1_axis + intercept1
    ax.plot(new_x1_axis, new_y1_axis)
  
    # Add labels and title
    ax.set_xticks(list(range(1850, 2100,25)))
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()