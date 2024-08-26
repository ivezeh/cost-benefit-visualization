import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

# Load the data from the CSV file
table = pd.read_csv('table.csv', index_col=0)

# Check for missing values and handle them (e.g., filling NaN with 0)
table['number of vehicles'].fillna(0, inplace=True)

# Ensure all values in 'number of vehicles' are integers
table['number of vehicles'] = table['number of vehicles'].astype(int)

# Calculate positions for labels and bars for visualization
table['pos_labels'] = table['number of vehicles'].cumsum() - table['number of vehicles'] / 2
table['pos_bars'] = table['pos_labels'] + np.arange(0, table.shape[0]) * 20
table['cost savings'] = table['price seller B'] - table['price seller A']

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(12, 10))
fig.set_facecolor("w")

# Use a specific matplotlib style for the plot
plt.style.use('fivethirtyeight')

# Initialize a list to hold colors for the bars
list_color = []

# Iterate over the data to determine the color and add labels based on cost savings
for num_cars, y, cost_save in zip(table['number of vehicles'], table['pos_bars'], table['cost savings']):
    if cost_save > 0:
        # If Seller A is cheaper, color the bar green
        ax.text(x=-200, y=y-10, s=f'({num_cars})', fontsize=10, ha='right')
        list_color.append('green')
    else:
        # If Seller B is cheaper, color the bar red
        ax.text(x=200, y=y-10, s=f'({num_cars})', fontsize=10, ha='left')
        list_color.append('red')

# Create a horizontal bar chart
ax.barh(table['pos_bars'], table['cost savings'], table['number of vehicles'], color=list_color, alpha=0.5)

# Add a vertical line at x = 0 for reference
plt.axvline(x=0, linestyle='--', linewidth=1)

# Add titles and labels
plt.title('Number of vehicles in ()', fontsize=12)
plt.suptitle('Cost savings', fontsize=18)
plt.xlabel('Difference in price between sellers B and A', fontsize=12)
plt.yticks(table['pos_bars'], table.index, fontsize=10)
plt.xticks(fontsize=10)

# Save the figure as a PDF
plt.savefig('cost_benefit.pdf', facecolor='w', bbox_inches="tight", dpi=600)

# Display the plot
plt.show()