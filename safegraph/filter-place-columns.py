import pandas as pd
import sys

df_final = pd.DataFrame(columns=["placekey", "naics_code"])
for i in range(1, 6):
    df = pd.read_csv("core_poi-part" + str(i) + ".csv")
    df_final = pd.concat((df_final, df.filter(items=["safegraph_place_id", "naics_code"])))
    print(i)
df_final.to_csv("places.csv", header=False)
