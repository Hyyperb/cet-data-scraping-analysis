import pandas as pd

df = pd.read_csv("./MeritList.csv")
df.set_index("Merit No", inplace=True)

for category in df["Category"].unique():
    df[df["Category"] == category].to_csv(
        f"category_wise_meritlists/{category.replace('/', '-')}MeritList.csv"
    )
