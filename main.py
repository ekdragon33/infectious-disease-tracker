import pandas as pd
import requests

print("🦠 Infectious Disease Tracker")
print("=" * 40)

url = "https://disease.sh/v3/covid-19/countries?sort=cases&limit=20"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
df = df[['country', 'cases', 'deaths', 'recovered', 'active']]

# Calculate death rate
df['death_rate'] = (df['deaths'].astype(float) /
                    df['cases'].astype(float) * 100).round(2)

print(f"\nTop 20 Countries — Death Rate Analysis\n")
print(df.to_string(index=False))

print(f"\nTotal cases tracked: {df['cases'].sum():,}")
print(f"Total deaths tracked: {df['deaths'].sum():,}")
print(f"Average death rate: {df['death_rate'].mean():.2f}%")