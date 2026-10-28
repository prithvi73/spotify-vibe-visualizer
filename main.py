import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the data
df = pd.read_csv("Data/spotify_history.csv")
print(df.head())

# Converting timestamp to standard date time
df["ts"] = pd.to_datetime(df["ts"])

# Filtering data to remove skips (ms_played should not be less than 30 seconds)
df = df[df["ms_played"] >= 30000] 