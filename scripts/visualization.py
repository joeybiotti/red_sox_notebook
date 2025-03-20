import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

red_sox_data = pd.read_csv('data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')

# Plotting the age distribution of Red Sox players
red_sox_data['Age'].hist(bins=10, color='red', edgecolor='black')
plt.title('Age Distribution of Red Sox Players')
plt.xlabel('Age')
plt.ylabel('Number of Players')

plt.savefig('./output/age_distribution.png')

# Plotting the age spread of Red Sox players
sns.boxplot(y='Age', color='red', data=red_sox_data)
plt.title('Age Spread of Red Sox Players')
plt.ylabel('Age')

plt.savefig('./output/age_spread.png')

print('Visualization complete!')