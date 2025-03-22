import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

script_dir =os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(script_dir, '../data/cleaned/Boston_Red_Sox_Roster_Data_cleaned.csv')

red_sox_data = pd.read_csv(csv_path)

# Plotting the age distribution of Red Sox players
red_sox_data['Age'].hist(bins=10, color='red', edgecolor='black')
plt.title('Age Distribution of Red Sox Players')
plt.xlabel('Age')
plt.ylabel('Number of Players')

output_dir = os.path.join(script_dir, '../output')
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'age_distribution.png'))

# Plotting the age spread of Red Sox players
sns.boxplot(y='Age', color='red', data=red_sox_data)
plt.title('Age Spread of Red Sox Players')
plt.ylabel('Age')

plt.savefig(os.path.join(output_dir, 'age_spread.png'))

print('Visualization complete!')