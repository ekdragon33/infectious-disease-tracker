import pandas as pd
import requests
import matplotlib.pyplot as plt

print("Fetching data...")

url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
df = pd.DataFrame(response.json())
df = df[['country', 'cases', 'deaths', 'active']]
df['death_rate'] = (df['deaths'].astype(float) / df['cases'].astype(float) * 100).round(2)

# Manually take top 15 by cases
top15 = df.sort_values('cases', ascending=False).head(15)
top15 = top15.sort_values('cases', ascending=True)  # flip so biggest is on top

# Chart 1: Top 15 by cases
plt.figure(figsize=(10, 8))
plt.barh(top15['country'], top15['cases'], color='steelblue')
plt.title('Top 15 Countries by Total Cases')
plt.xlabel('Total Cases')
plt.tight_layout()
plt.savefig('cases_chart.png')
plt.show()

# Chart 2: Death rates for same countries
plt.figure(figsize=(10, 8))
plt.barh(top15['country'], top15['death_rate'], color='crimson')
plt.title('Death Rate by Country (%)')
plt.xlabel('Death Rate %')
plt.tight_layout()
plt.savefig('death_rate_chart.png')
plt.show()

print("Done!")