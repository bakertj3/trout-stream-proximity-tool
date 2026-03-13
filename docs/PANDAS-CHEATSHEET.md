# pandas CHEATSHEET

## Basics

- pd.DataFrame({}) - create from dictionary
- .shape - gets # rows x # columns of DataFrame
- .columns - gets list of column names in DataFrame
- .head(n) - return n records from beginning of the DataFrame

## Filtering

- data[data["col"] == value] - boolean indexing
- data.loc[lambda df: df["col"] == value] - lambda approach
- .str.contains() - find values that contain matching criteria
- .idxmax() - returns the index of the max value for the attribute in question

## Common Operations

- .unique() - returns array of unique values for input array(series)
- .value_counts() - returns value counts of each DataSeries or column sorted descending by count
- .sort_values(by=["col"]) - sorts DataFrame by "col", asc by default
- .max(), .min() - max(highest)/min(lowest) value in a DataSeries or column

## Data Manipulation

- pd.json_normalize() - flattens nested json dictionary data for simpler access
