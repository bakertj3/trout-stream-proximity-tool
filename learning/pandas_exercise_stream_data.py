import pandas as pd

stream_data = pd.read_json("data/Class A Trout Streams.geojson")


features = stream_data["features"]
print(type(features))

print(stream_data["features"][0]["properties"]["WtrName"])

stream_details = pd.json_normalize(features)


print("------------------ STREAM DATA DETAILS ------------------")
print("--- ALL DATA ---")
print(stream_details)
print("--- COLUMNS ---")
print(stream_details.columns)
print("--- SHAPE ---")
print(stream_details.shape)
print("--- Total # Stream Records ---")
print(stream_details["id"].count())
print("--- count of unique stream names ---")
name_array = stream_details["properties.WtrName"].unique()
print(len(name_array))

print("--- Counties with the most streams ---")
streams_per_county= stream_details["properties.COUNTY_NAM"].value_counts()
print(streams_per_county.head(5))

print("--- Stream Details filtered to Centre County ---")
centre_county = stream_details[stream_details["properties.COUNTY_NAM"] == "Centre"]
print(centre_county)

print("--- Streams with creek in the name ---")
streams_with_creek_in_name = stream_details[stream_details["properties.WtrName"].str.contains("creek", case=False)]
print(streams_with_creek_in_name["properties.WtrName"])

print("--- Stream with longest name ---")
longest_stream_index = stream_details["properties.WtrName"].str.len().idxmax()
print(stream_details.loc[longest_stream_index, "properties.WtrName"])

print(stream_data["features"][0]["geometry"].keys())