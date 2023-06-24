import pandas as pd
import matplotlib.pyplot as plt

# Read the data from Excel file
data = pd.read_excel('C:\Users\Lenovo\Downloads\dailyCalories_merged.xlsx')

# Calculate the cumulative steps
data['CumulativeSteps'] = data['TotalSteps'].cumsum()

# Plot the cumulative steps over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['CumulativeSteps'], marker='o', linestyle='-', color='blue')
plt.title('Cumulative Steps')
plt.xlabel('ActivityDate')
plt.ylabel('Cumulative Steps')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
