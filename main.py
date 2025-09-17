# INF601 - Advanced Programming in Python
# Nicholas Kitchen
# Mini Project 2

# My question: Which country had the highest increase in GDP from 2020 to 2025? What were the top 5?
# Note: If a country does not have data available for 2020 or 2025, they will be excluded.
#       As of 9/17/2025, ['Afghanistan', 'Eritrea', 'Lebanon', 'Pakistan', 'Sri Lanka', 'Syria', 'Palestine'] do not have sufficient data.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Read in csv dataset
df = pd.read_csv("./data/2020-2025.csv")

# Create charts folder if it does not exist
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

# Remove any country that does not have data for the years 2020 and 2025
df = df.dropna().reset_index(drop=True)

# Create a new column "delta" to find the change in GDP from 2020 to 2025
df["delta"] = df["2025"] - df["2020"]

# Get the row of the country with the highest GDP increase along with the top 5
highest_increase_country = df.loc[df["delta"].idxmax()]
top5_countries = df.nlargest(5, "delta")

# Create a graph that shows the GDP of each year for the top 5 countries
years = ["2020", "2021", "2022", "2023", "2024", "2025"]

fig, ax = plt.subplots(figsize=(8,5))

for _, row in top5_countries.iterrows():
    ax.plot(years, row[years] / 1_000_000, marker="o", label=row["Country"])

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

ax.set_ylabel("GDP (in millions)")
ax.set_xlabel("Year")
ax.set_title("Top 5 Highest Increase Countries - GDP by Year")
ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")

ax.set_ylim(0, 33)
ax.set_yticks(np.arange(0, 33, 2.5))

plt.tight_layout()
plt.savefig(f'charts/Top_5_Countries_-_GDP_by_Year.png')
print(f'Saving Top_5_Countries_-_GDP_by_Year.png to charts folder.')

# Create a graph that shows the GDP growth of the top 5 countries from 2020 to 2025
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(top5_countries["Country"], top5_countries["delta"] / 1_000_000)

ax.set_ylabel("Delta (in millions)")
ax.set_xlabel("Country")
ax.set_title("GDP Growth from 2020 to 2025")
plt.xticks(rotation=30, ha="right")

ax.set_ylim(0, 10)
ax.set_yticks(np.arange(0, 11, 1))

plt.tight_layout()
plt.savefig(f'charts/GDP_Growth_from_2020_to_2025.png')
print(f'Saving GDP_Growth_from_2020_to_2025.png to charts folder.')

print()
print("The country with the highest GDP growth between 2020 and 2025 is:")
print(highest_increase_country[["Country", "2020","2025", "delta"]])
print()
print("The top 5 countries with the highest GDP growth between 2020 and 2025 are:")
print(top5_countries[["Country", "2020","2025", "delta"]])
