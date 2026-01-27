# /// script
# dependencies = [
#   "pandas",
#   "pyarrow",
# ]
# ///

import pandas as pd

df = pd.read_parquet("/home/ramesh/DataProjects/DE-Zoomcamp/Module1/data/green_tripdata_2025-11.parquet")
df.to_csv("/home/ramesh/DataProjects/DE-Zoomcamp/Module1/data/green_tripdata_2025-11.csv", index=False)
print("Conversion complete!")