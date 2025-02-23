import pandas as pd
import json

df = pd.read_excel("/Users/harishprabhu/Desktop/Web_Scraping/vivo_data.xlsx")
# print(df.shape)
print(df[0:1])

df["data-track"] = df["data-track"].str.replace("{", "").replace("}", "")
df["data-track"] = df["data-track"].str.replace('"', '').str.replace("params:", "")
split_data = df["data-track"].str.split(",", expand=True)

# df["type"] = df["data-track"].str.extract(r'type:([\w-]+)')
df_split = split_data.apply(lambda x: dict(item.split(":") for item in x.dropna()), axis=1)
df_final = pd.DataFrame(df_split.tolist())

# print(df[0:1])
# print(split_data)
# print(df_split)
# print(df_final)

# Saving to csv (excel)
df_final.to_excel("Vivo_final.xlsx")