import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importing data 
df = pd.read_csv('./fcc-forum-pageviews.csv',index_col='date',parse_dates=True) 

# Cleaning data
df = df[(df.value > df.value.quantile(0.025)) & (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    # Drawing line plot
    fig, ax = plt.subplots(1,1,figsize = (16,6))
    ax.plot(df.index, df.value)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Saving image and returning figure
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copying and modifying data for the monthly bar plot
    df_bar = df.value.groupby([df.index.year,df.index.month_name()]).mean()
    df_bar.index.names = ['Years', 'Months']
    df_bar = df_bar.reset_index(name='Average Page Views')

    # Drawing bar plot
    bar_plot = sns.catplot(x='Years',y='Average Page Views',hue='Months', hue_order=['January','February','March','April','May','June','July','August', 'September','October','November','December'],data=df_bar, kind='bar',legend_out=False, height=6, aspect=1.5)
    fig = bar_plot.fig

    # Saving image and returning figure 
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Preparing data for box plots 
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.rename({'year':'Year','month':'Month','value':'Page Views'},axis= 'columns',inplace = True)

    # Drawing box plots (using Seaborn)
    fig, (yearwise,monthwise)= plt.subplots(1,2,figsize=(12,6))
    yearwise.set_title('Year-wise Box Plot (Trend)')
    monthwise.set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(x='Year',y='Page Views',data=df_box,ax=yearwise)
    sns.boxplot(x='Month',y='Page Views',order=['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],data=df_box,ax=monthwise)
    
    # Saving image and returning figure 
    fig.savefig('box_plot.png')
    return fig
