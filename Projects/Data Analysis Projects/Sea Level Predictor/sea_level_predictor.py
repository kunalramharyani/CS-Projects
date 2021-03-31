import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Reading data from file
    df = pd.read_csv('./epa-sea-level.csv') 

    # Creating scatter plot
    x_axis = df.Year
    y_axis = df.iloc[:,1]
    plt.scatter(x_axis,y_axis)
    
    # Creating first line of best fit
    lr1 = linregress(x_axis,y_axis)
    x_w_lr1 = x_axis.append(pd.Series(range(x_axis[len(x_axis)-1]+1,2050)))
    plt.plot(x_w_lr1, lr1.intercept+lr1.slope*x_w_lr1)

    # Creating second line of best fit
    x_recent_year = x_axis[x_axis>=2000]
    y_recent_year = y_axis[x_axis[x_axis==2000].index[0]:]
    lr2 = linregress(x_recent_year,y_recent_year)
    x_w_lr2_recent = x_recent_year.append(pd.Series(range(x_axis[len(x_axis)-1]+1,2050)))
    plt.plot(x_w_lr2_recent, lr2.intercept+lr2.slope*x_w_lr2_recent)


    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Saving plot and returning data for testing 
    plt.savefig('sea_level_plot.png')
    return plt.gca()