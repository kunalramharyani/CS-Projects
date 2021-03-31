import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importing data
df = pd.read_csv('./medical_examination.csv')

# Adding overweight column
bmi = df.weight / (df.height/100)**2
overweightlist = []
for individual_bmi in bmi:
  if individual_bmi > 25:
    overweightlist.append(1)
  else:
    overweightlist.append(0)
df['overweight'] = overweightlist

# Normalizing data
norm_val = df.loc[:,['cholesterol','gluc']] > 1
df.loc[:,['cholesterol','gluc']] = norm_val.astype(int)

# Drawing Categorical Plot
def draw_cat_plot():
    # Creating DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Grouping and reformatting the data to split it by 'cardio'
    cardio_val_0 = df_cat[df_cat.cardio == 0].variable.groupby(df_cat.value).value_counts()
    cardio_val_0 = cardio_val_0.reset_index(name='total')
    cardio_val_0['cardio'] = 0

    cardio_val_1 = df_cat[df_cat.cardio ==1].variable.groupby(df_cat.value).value_counts()
    cardio_val_1 = cardio_val_1.reset_index(name='total')
    cardio_val_1['cardio'] = 1

    df_cat = cardio_val_0.append(cardio_val_1)

    # Drawing the catplot with 'sns.catplot()'
    catplot_fig = sns.catplot(x='variable',y='total',hue='value', order=sorted(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']),data=df_cat,col='cardio', kind='bar')

    fig = catplot_fig.fig

    # Returning figure
    fig.savefig('catplot.png')
    return fig


# Drawing Heat Map
def draw_heat_map():

    # Cleaning the data
    clean_rule1 = np.where((df['ap_lo'] > df['ap_hi']))[0]
    clean_rule2 = np.where(df['height'] < df['height'].quantile(0.025))[0]
    clean_rule3 = np.where(df['height'] > df['height'].quantile(0.975))[0]
    clean_rule4 = np.where(df['weight'] < df['weight'].quantile(0.025))[0]
    clean_rule5 = np.where(df['weight'] > df['weight'].quantile(0.975))[0]
    clean_all = np.unique(np.concatenate([clean_rule1,clean_rule2,clean_rule3,clean_rule4,clean_rule5]))

    df_heat = df.drop(clean_all)

    # Calculating the correlation matrix
    corr = df_heat.corr()

    # Generating a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, vmax=.3, center=0, annot=True, fmt='.1f',
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    # Returning figure
    fig.savefig('heatmap.png')
    return fig