# INF601 - Advanced Programming in Python
# Nicholas Kitchen
# Mini Project 2

# My question: Which country has had the highest increase in GDP from 2020 and 2025? What were the top 5?
# Note: If a country does not have data available for 2020 or 2025, they will be excluded.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read in csv dataset
df = pd.read_csv("./data/2020-2025.csv")

# Remove any country that does not have data for the years 2020 and 2025
df = df.dropna().reset_index(drop=True)

# Create a new column "delta" to find the change between GDP in 2020 and 2025
df["delta"] = df["2025"] - df["2020"]

# Get the row of the country with the highest GDP increase
highest_increase_country = df.loc[df["delta"].idxmax()]
top5_highest_increase_countries = df.nlargest(5, "delta")

# Create a graph that shows the GDP of each year for the top 5 countries
years = ["2020", "2021", "2022", "2023", "2024", "2025"]

fig, ax = plt.subplots(figsize=(8,5))

for _, row in top5_highest_increase_countries.iterrows():
    ax.plot(years, row[years] / 1_000_000, marker="o", label=row["Country"])

ax.set_ylim(0, top5_highest_increase_countries[years].max().max() / 1_000_000 * 1.1)
ax.set_ylabel("GDP (in millions)")
ax.set_xlabel("Year")
ax.set_title("Top 5 Countries - GDP by Year")
ax.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.show()

# Create a graph that shows the GDP growth of the top 5 countries from 2020 to 2025
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(top5_highest_increase_countries["Country"], top5_highest_increase_countries["delta"] / 1_000_000)

ax.set_ylabel("Delta (in millions)")
ax.set_xlabel("Country")
ax.set_title("GDP Growth from 2020 to 2025")
plt.xticks(rotation=30, ha="right")

ax.set_ylim(0, 10)
ax.set_yticks(np.arange(0, 11, 1))

plt.tight_layout()
plt.show()

print("The country with the highest GDP growth between 2020 and 2025 is:")
print(highest_increase_country[["Country", "2020","2025", "delta"]])
print()
print("The top 5 countries with the highest GDP growth between 2020 and 2025 are:")
print(top5_highest_increase_countries[["Country", "2020","2025", "delta"]])

# Please submit a link to your GitHub project. Do not submit your project files here!
#
# This project will be using Pandas dataframes. This isn't intended to be full blown data science project. The goal here is to come up with some question and then see what API or datasets you can use to get the information needed to answer that question. This will get you familar with working with datasets and asking questions, researching APIs and gathering datasets. If you get stuck here, please email me!
#
# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (5/5 points) Proper import of packages used.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

