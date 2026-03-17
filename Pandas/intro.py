import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Japan', 'New York', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print(df)


# df = pd.read_csv("data.csv")




## read and update operation

df["Age"] = df["Age"] + 1


df.drop(1, axis=0, inplace=True)

print(df)





## other functions in pandas

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)

df.dropna()

df.sort_values(by="Age")



#  df.groupby("column_name")["target_column"].agg(function())

df.groupby("City")["Age"].agg("mean", "min", "max")

print(df)

print(df["City"].value_counts())



data1 = {
    'Name': ['Frank', 'Grace'],
    'Age': [50, 55],
    'City': ['Chicago', 'Los Angeles']
}

df1 = pd.DataFrame(data1)




# Concatenating two DataFrames
df_combined = pd.concat([df, df1], ignore_index=True)

print(df_combined)

print(df_combined[['City', 'Age']].head())

pivot = pd.pivot_table(df_combined, values="Age", index="City", aggfunc="mean")

print(pivot)

df_combined.to_csv("output.csv", index=False)




# conditional filtering

print(df[(df["Age"] > 25) & (df["City"] == "New York")])