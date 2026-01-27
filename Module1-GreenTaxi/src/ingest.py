import pandas as pd
from db import get_engine

engine = get_engine()

# CSV
df_csv = pd.read_csv("data/taxi_zone_lookup.csv")
df_csv.to_sql("taxi_zone_lookup", engine, if_exists="replace", index=False)

# Parquet
df_parquet = pd.read_parquet("data/green_tripdata_2025-11.parquet")
df_parquet.to_sql("green_trips_parquet", engine, if_exists="replace", index=False)

print("Ingestion complete")
