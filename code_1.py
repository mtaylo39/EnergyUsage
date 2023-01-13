import pandas as pd

url = 'https://raw.githubusercontent.com/mtaylo39/EnergyUsage/main/weather.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))

