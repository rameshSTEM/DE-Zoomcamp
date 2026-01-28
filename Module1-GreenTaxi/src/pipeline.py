import pandas as pd
from sqlalchemy import create_engine

def main():
    print("Pipeline starting…")

    df = pd.DataFrame({"a": [1, 2, 3]})
    print(df)

if __name__ == "__main__":
    main()
