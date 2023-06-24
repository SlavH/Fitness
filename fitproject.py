import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse

# Load the dataset
dailyActivity_merged = pd.read_csv(r"C:\Users\Lenovo\Downloads\dailyActivity_merged.csv")

# Convert the ActivityDate column to datetime format
dailyActivity_merged["ActivityDate"] = dailyActivity_merged["ActivityDate"].apply(lambda x: parse(x, dayfirst=False, yearfirst=False))

# Calculate total distance for each activity intensity level
activity_intensity = ["VeryActiveDistance", "ModeratelyActiveDistance", "LightActiveDistance"]
activity_distances = dailyActivity_merged[activity_intensity].sum().values

# Normalize the distances to create a percentage distribution
total_distance = activity_distances.sum()
activity_percentage = (activity_distances / total_distance) * 100

# Calculate the weekday from the ActivityDate column

# Normalize the distances to create a percentage distribution
total_distance = activity_distances.sum()
activity_percentage = (activity_distances / total_distance) * 100

# Calculate the weekday from the ActivityDate column
dailyActivity_merged["DayOfWeek"] = dailyActivity_merged["ActivityDate"].dt.day_name()

# Calculate total distance for each activity intensity level
activity_intensity = ["VeryActiveDistance", "ModeratelyActiveDistance", "LightActiveDistance"]
activity_distances = dailyActivity_merged[activity_intensity].sum().values

# Normalize the distances to create a percentage distribution
total_distance = activity_distances.sum()
activity_percentage = (activity_distances / total_distance) * 100

# Data visualization

# Stacked Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(activity_intensity, activity_distances, color=["skyblue", "lightgreen", "orange"])
plt.xlabel("Activity Intensity")
plt.ylabel("Total Distance (in miles)")
plt.title("Distribution of Activity Intensity")
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(dailyActivity_merged["TotalSteps"], dailyActivity_merged["Calories"], alpha=0.5, color="skyblue")
plt.xlabel("Total Steps")
plt.ylabel("Calories")
plt.title("Total Steps vs Calories")
plt.show()

activity_categories = ["VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes", "SedentaryMinutes"]
activity_minutes = dailyActivity_merged[activity_categories].sum().values

# Stacked Bar Chart: Activity Minutes
plt.figure(figsize=(10, 6))
bars = plt.bar(activity_categories, activity_minutes, color=["skyblue", "lightgreen", "orange", "red"])
plt.xlabel("Activity Category")
plt.ylabel("Total Minutes")
plt.title("Distribution of Activity Minutes")

# Add tags on each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, int(height), ha='center', va='bottom')

plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(dailyActivity_merged["VeryActiveMinutes"], dailyActivity_merged["Calories"], alpha=0.5, color="skyblue")
plt.xlabel("Very Active Minutes")
plt.ylabel("Calories")
plt.title("Very Active Minutes vs Calories")
plt.show()

# Scatter Plot: FairlyActiveMinutes vs Calories
plt.figure(figsize=(8, 6))
plt.scatter(dailyActivity_merged["FairlyActiveMinutes"], dailyActivity_merged["Calories"], alpha=0.5, color="lightgreen")
plt.xlabel("Fairly Active Minutes")
plt.ylabel("Calories")
plt.title("Fairly Active Minutes vs Calories")
plt.show()

# Scatter Plot: LightlyActiveMinutes vs Calories
plt.figure(figsize=(8, 6))
plt.scatter(dailyActivity_merged["LightlyActiveMinutes"], dailyActivity_merged["Calories"], alpha=0.5, color="orange")
plt.xlabel("Lightly Active Minutes")
plt.ylabel("Calories")
plt.title("Lightly Active Minutes vs Calories")
plt.show()

# Scatter Plot: SedentaryMinutes vs Calories
plt.figure(figsize=(8, 6))
plt.scatter(dailyActivity_merged["SedentaryMinutes"], dailyActivity_merged["Calories"], alpha=0.5, color="red")
plt.xlabel("Sedentary Minutes")
plt.ylabel("Calories")
plt.title("Sedentary Minutes vs Calories")
plt.show()

food_and_calories = pd.read_csv(r"C:\Users\Lenovo\Downloads\Food_and_Calories.csv")
def calculate_calories(food_data):
    # Initialize empty lists for daily and weekly calories
    daily_calories = []
    weekly_calories = []

    # Prompt the user for input
    num_days = int(input("Enter the number of days: "))

    for day in range(1, num_days + 1):
        daily_calories_sum = 0

        print(f"\n--- Day {day} ---")
        num_meals = int(input("Enter the number of meals: "))

        for meal in range(1, num_meals + 1):
            food = input(f"Enter the food for meal {meal}: ")
            portion = float(input("Enter the serving portion: "))

            # Lookup the calories for the food in the dataframe
            calories = food_data.loc[food_data["Food"] == food, "Calories"].values

            if len(calories) > 0:
                # Calculate the calories consumed for the specific food and portion
                calories_consumed = calories[0] * portion
                daily_calories_sum += calories_consumed
            else:
                print(f"No calorie information found for {food}.")

        # Append the daily calories to the list
        daily_calories.append(daily_calories_sum)

    # Calculate the weekly calories
    weekly_calories = [sum(daily_calories[:i+1]) for i in range(len(daily_calories))]
    weekly_calories_avg = sum(weekly_calories) / num_days

    return daily_calories, weekly_calories, weekly_calories_avg

# Calculate daily and weekly calories
daily_calories, weekly_calories, weekly_calories_avg = calculate_calories(food_and_calories)

# Plot daily calorie consumption
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(daily_calories) + 1), daily_calories, marker="o", color="skyblue")
plt.xlabel("Day")
plt.ylabel("Calories")
plt.title("Daily Calorie Consumption")
plt.show()
