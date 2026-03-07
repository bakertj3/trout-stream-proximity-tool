import pandas as pd

df = pd.DataFrame({
    "Stream_Names":["Spring Creek", "Penns Creek", "Pine Creek"],
    "Counties": ["Centre", "Centre", "Lycoming"],
    "Lengths (miles)": [13.5, 45.2, 87.2]
}
)
data = df
#print(df)
#print(data.shape)
#print(data.columns)
#print(data.head(2))

Stream_Names = data["Stream_Names"]
print(Stream_Names)

Two_Columns = data[["Stream_Names","Counties"]]
print(Two_Columns)

centre_streams = data[data["Counties"]=="Centre"]
print(centre_streams)

twenty_or_greater = data[data["Lengths (miles)"] > 20]
print(twenty_or_greater)

print(data["Counties"].unique())

print(data["Counties"].value_counts())

print(data.sort_values(by=["Lengths (miles)"]))

lengths=data["Lengths (miles)"]
print(lengths.max())

print(data.groupby("Counties")["Lengths (miles)"].max())
print(data.max())

